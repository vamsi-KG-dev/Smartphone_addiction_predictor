# 📚 Book Recommendation System

This is a **Book Recommendation System** built with machine learning and deployed using **Streamlit Community Cloud**. The app recommends books based on user input and provides insights like popular books, books with maximum discounts, and more.

---

## 🚀 Features

- **Personalized Recommendations**: Suggests books similar to the selected one.
- **Top Books Insights**:
  - Top 10 books based on ratings.
  - Top 10 books offering maximum discounts.
  - Top 10 books at the least price.
  - Top 10 books by maximum checkouts.
- **Interactive UI**: Built using Streamlit for a seamless user experience.

---

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **Streamlit**: Web application framework for the frontend.
- **Machine Learning**: Trained model to calculate similarity scores.
- **Pandas & NumPy**: Data manipulation and analysis.
- **Pickle**: Storing serialized model and data files.

---

## 📂 Project Structure

📁 Project Folder ├── app.py # Streamlit app script ├── requirements.txt # Dependencies ├── df_new.pkl # Pivot table data ├── df.pkl # Dataset file ├── similarity_scores.pkl # Trained similarity scores ├── df1_new1.pkl # Popular books data ├── df2_new1.pkl # Discounted books data ├── df3_new1.pkl # Least priced books data ├── df4_new1.pkl # Books by checkouts data


## 🖥️ How to Run Locally

1. **Clone the Repository**:
   
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name

2. **Install Dependencies: Make sure you have Python installed, then run**:

  pip install -r requirements.txt

3. **Run the App**:
  streamlit run app.py

4. **Open your browser and navigate to http://localhost:8501.**



