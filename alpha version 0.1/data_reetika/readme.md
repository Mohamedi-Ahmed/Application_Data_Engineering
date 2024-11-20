- create venv with pyhton use commands for cmd:

  # For Windows

  **python -m venv myenv** ------ if python is not recognized check with **py -m venv myenv**
  **myenv\Scripts\activate**

  # For macOS/Linux

  python3 -m venv myenv
  source myenv/bin/activate
- **pip install -r requirements.txt**
- navigate to the location where you have your streamlit app.py and execute

  - **streamlit run app.py**
