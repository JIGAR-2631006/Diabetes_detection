{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5b2740b3-f318-4183-88b0-da4ff60aaca2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: streamlit in c:\\programdata\\anaconda3\\lib\\site-packages (1.37.1)\n",
      "Requirement already satisfied: numpy in c:\\programdata\\anaconda3\\lib\\site-packages (1.26.4)\n",
      "Requirement already satisfied: pandas in c:\\programdata\\anaconda3\\lib\\site-packages (2.2.2)\n",
      "Requirement already satisfied: scikit-learn in c:\\programdata\\anaconda3\\lib\\site-packages (1.5.1)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (24.1)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (10.4.0)\n",
      "Collecting protobuf<6,>=3.20 (from streamlit)\n",
      "  Downloading protobuf-5.29.5-cp310-abi3-win_amd64.whl.metadata (592 bytes)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (16.1.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (13.7.1)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (8.2.3)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\lenovo\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (4.15.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: watchdog<5,>=2.1.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: scipy>=1.6.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from scikit-learn) (1.13.1)\n",
      "Requirement already satisfied: joblib>=1.2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from scikit-learn) (1.4.2)\n",
      "Requirement already satisfied: threadpoolctl>=3.1.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from scikit-learn) (3.5.0)\n",
      "Requirement already satisfied: jinja2 in c:\\programdata\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: toolz in c:\\programdata\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\programdata\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: six>=1.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\lenovo\\appdata\\roaming\\python\\python312\\site-packages (from requests<3,>=2.27->streamlit) (2.6.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\lenovo\\appdata\\roaming\\python\\python312\\site-packages (from requests<3,>=2.27->streamlit) (2026.1.4)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\lenovo\\appdata\\roaming\\python\\python312\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.4.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\programdata\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\programdata\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Downloading protobuf-5.29.5-cp310-abi3-win_amd64.whl (434 kB)\n",
      "Installing collected packages: protobuf\n",
      "  Attempting uninstall: protobuf\n",
      "    Found existing installation: protobuf 6.33.2\n",
      "    Uninstalling protobuf-6.33.2:\n",
      "      Successfully uninstalled protobuf-6.33.2\n",
      "Successfully installed protobuf-5.29.5\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit numpy pandas scikit-learn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fadfaa3a-de29-4f28-8818-8b1c3ff6e3c8",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'diabetes_model.pkl'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 9\u001b[0m\n\u001b[0;32m      6\u001b[0m st\u001b[38;5;241m.\u001b[39mset_page_config(page_title\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mDiabetes Prediction\u001b[39m\u001b[38;5;124m\"\u001b[39m, page_icon\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m🩺\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      8\u001b[0m \u001b[38;5;66;03m# Load trained model\u001b[39;00m\n\u001b[1;32m----> 9\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mopen\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdiabetes_model.pkl\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mrb\u001b[39m\u001b[38;5;124m\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m file:\n\u001b[0;32m     10\u001b[0m     model \u001b[38;5;241m=\u001b[39m pickle\u001b[38;5;241m.\u001b[39mload(file)\n\u001b[0;32m     12\u001b[0m \u001b[38;5;66;03m# App title\u001b[39;00m\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:324\u001b[0m, in \u001b[0;36m_modified_open\u001b[1;34m(file, *args, **kwargs)\u001b[0m\n\u001b[0;32m    317\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m}:\n\u001b[0;32m    318\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m    319\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIPython won\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m by default \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    320\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    321\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myou can use builtins\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m open.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    322\u001b[0m     )\n\u001b[1;32m--> 324\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m io_open(file, \u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'diabetes_model.pkl'"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Page config\n",
    "st.set_page_config(page_title=\"Diabetes Prediction\", page_icon=\"🩺\")\n",
    "\n",
    "# Load trained model\n",
    "with open(\"diabetes_model.pkl\", \"rb\") as file:\n",
    "    model = pickle.load(file)\n",
    "\n",
    "# App title\n",
    "st.title(\"🩺 Diabetes Prediction System\")\n",
    "st.write(\"Predict whether a person has Diabetes using ML\")\n",
    "\n",
    "st.subheader(\"Enter Patient Details\")\n",
    "\n",
    "# Input fields\n",
    "pregnancies = st.number_input(\"Pregnancies\", min_value=0, max_value=20)\n",
    "glucose = st.number_input(\"Glucose Level\", min_value=0, max_value=200)\n",
    "bp = st.number_input(\"Blood Pressure\", min_value=0, max_value=150)\n",
    "skin = st.number_input(\"Skin Thickness\", min_value=0, max_value=100)\n",
    "insulin = st.number_input(\"Insulin\", min_value=0, max_value=900)\n",
    "bmi = st.number_input(\"BMI\", min_value=0.0, max_value=70.0)\n",
    "dpf = st.number_input(\"Diabetes Pedigree Function\", min_value=0.0, max_value=3.0)\n",
    "age = st.number_input(\"Age\", min_value=0, max_value=120)\n",
    "\n",
    "# Predict button\n",
    "if st.button(\"Predict Diabetes\"):\n",
    "    input_data = np.array([[pregnancies, glucose, bp, skin,\n",
    "                             insulin, bmi, dpf, age]])\n",
    "\n",
    "    prediction = model.predict(input_data)\n",
    "\n",
    "    if prediction[0] == 1:\n",
    "        st.error(\"⚠️ High chance of Diabetes\")\n",
    "    else:\n",
    "        st.success(\"✅ Low chance of Diabetes\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cb087d39-b70b-4b2b-aff1-aa5576ef14ae",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
