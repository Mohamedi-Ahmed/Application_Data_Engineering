import streamlit as st
import polars as pl
import plotly.express as px

def main():
    st.set_page_config(page_title="Lecteur de Fichiers", page_icon="📊", layout="wide")

    st.title("Lecteur de Fichiers CSV, TSV et Parquet")
    st.markdown(
        """
        **Cette application vous permet de :**
        - Charger des fichiers aux formats CSV, TSV ou Parquet.
        - Explorer les données et obtenir des informations sur leurs colonnes.
        - Visualiser les types de données et la qualité des données (valeurs nulles, manquantes).
        """
    )

    uploaded_file = st.file_uploader("Chargez votre fichier ici", type=["csv", "tsv", "parquet"])

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1]
        
        try:
            if file_extension == 'csv':
                df = pl.read_csv(uploaded_file)
            elif file_extension == 'tsv':
                df = pl.read_csv(uploaded_file, sep='\t')
            elif file_extension == 'parquet':
                df = pl.read_parquet(uploaded_file)
            else:
                st.error("❌ Format de fichier non pris en charge.")
                return

            st.write("### Aperçu des Données")
            st.dataframe(df, use_container_width=True)

            st.write(f"**Nombre de lignes :** {df.shape[0]}")
            st.write(f"**Nombre de colonnes :** {df.shape[1]}")

            st.write("### Informations sur les Colonnes")
            column_info = pl.DataFrame({
                "Nom de la Colonne": df.columns,
                "Type de Donnée": [str(dtype) for dtype in df.dtypes],
                "Valeurs Nulles": [df[col].null_count() for col in df.columns],
                "Valeurs Uniques": [df[col].n_unique() for col in df.columns]
            })
            st.dataframe(column_info, use_container_width=True)

            st.write("### Graphique des Valeurs Nulles")
            null_values = column_info[["Nom de la Colonne", "Valeurs Nulles"]]
            
            if null_values["Valeurs Nulles"].sum() > 0:
                fig = px.bar(
                    null_values,
                    x="Nom de la Colonne",
                    y="Valeurs Nulles",
                    title="Nombre de Valeurs Nulles par Colonne",
                    labels={"Nom de la Colonne": "Colonnes", "Valeurs Nulles": "Nombre de Valeurs Nulles"},
                    text_auto=True
                )
                fig.update_layout(xaxis_tickangle=-45, title_x=0.5)  # Rotation des labels et centrage du titre
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.success("Aucune valeur manquante trouvée dans le dataset !")

        except Exception as e:
            st.error(f"❌ Erreur lors de la lecture du fichier : {e}")
    else:
        st.info("Veuillez charger un fichier pour commencer.")

if __name__ == "__main__":
    main()
