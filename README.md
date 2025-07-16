# 📰 Fake News Prediction using Machine Learning

A machine learning application that classifies news articles as **real** or **fake** using Natural Language Processing (NLP) techniques and a logistic regression model.

---

## 🚀 Project Overview

This project addresses the problem of fake news detection by training a model to classify the authenticity of news articles. It includes data preprocessing, TF-IDF vectorization, model training, and a Streamlit-powered user interface for real-time predictions.

---

## 💻 Tech Stack

- **Python**
- **scikit-learn** – For logistic regression and model evaluation
- **Streamlit** – For building the interactive web interface
- **Pandas / NumPy** – Data handling and transformations
- **TF-IDF Vectorizer** – For text feature extraction
- **Pickle** – For saving the trained model and vectorizer

---

## 📄 What's Inside

- `fake_news_model.pkl`  
  Trained logistic regression model saved with Pickle.

- `vectorizer.pkl`  
  TF-IDF vectorizer used to convert input text to feature vectors.

- `app.py`  
  Main Streamlit app that accepts user input and displays predictions.

- `requirements.txt`  
  Contains required Python libraries:
  ```
  streamlit
  pandas
  numpy
  scikit-learn
  ```

---

## 🧠 How It Works

1. News text is entered by the user in the app.
2. The input is processed using a saved TF-IDF vectorizer.
3. The logistic regression model predicts:
   - **0** → Fake news  
   - **1** → Real news
4. The result is displayed immediately in the UI.

---

## 📦 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sjapanjots/fake_news_prediction_ml.git
   cd fake_news_prediction_ml
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   streamlit run app.py
   ```

4. Go to `http://localhost:8501` in your browser to use the app.

---

## ✅ Example Usage

- **Input**:
  ```
  The Prime Minister has announced new economic reforms during a press conference...
  ```

- **Output**:  
  ✅ **Real News**

---

## 🙋‍♂️ Author

**Japanjot Singh**  
Data Scientist & ML Enthusiast  
📬 sjapanjots@gmail.com