 # 🎬 Movie Recommendation System

## 📌 Project Overview

This project is a **Content-Based Movie Recommendation System** built using Machine Learning techniques.
It recommends the **top 5 similar movies** based on the user’s input.

The system analyzes movie features such as **overview, genres, keywords, cast, and crew** to find similarities and provide accurate recommendations.

---

## 🚀 Features

* 🎯 Recommend top 5 similar movies
* 🔍 Search movie names (case-insensitive)
* 🧠 Uses content-based filtering technique
* ⚡ Fast similarity computation using vectorization
* ❌ Handles invalid user input gracefully
* 💬 Interactive command-line interface

---

## 🧠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK

---

## ⚙️ How It Works

1. **Data Collection**

   * TMDB 5000 Movies Dataset

2. **Data Preprocessing**

   * Removed missing values
   * Converted JSON-like text into Python objects using `ast`

3. **Feature Engineering**

   * Selected important features:

     * Overview
     * Genres
     * Keywords
     * Cast
     * Crew
   * Combined them into a single column called **tags**

4. **Text Vectorization**

   * Used `CountVectorizer` to convert text into numerical vectors

5. **Similarity Calculation**

   * Used **Cosine Similarity** to measure similarity between movies

6. **Recommendation System**

   * Based on user input, the system finds and returns the top 5 similar movies

---

## ▶️ How to Run the Project

```bash
pip install -r requirements.txt
python main.py
```

---

## 💻 Sample Output

```
Hello, enter your movie name: avatar

🎬 These are your recommended movies:

1) Titanic
2) The Avengers
3) The Dark Knight
4) Inception
5) Interstellar

🍿 Enjoy your movies!
```

---

## 📸 Output Screenshot

 <img width="1920" height="1080" alt="Screenshot 2026-04-21 144044" src="https://github.com/user-attachments/assets/2f9dcea8-8516-4007-b3c1-f1d6f57139ff" />

```
![Output](screenshots/output.png)
```

---

## 📊 Dataset

Due to file size limitations, the dataset is not included in this repository.

Download it from:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## 📁 Project Structure

```
movie-recommendation-system/
│
├── main.py
├── requirements.txt
├── README.md
├── screenshots/
│   └── output.png
└── .gitignore
```

---

## 🌟 Future Improvements

* 🎨 Build a web app using Streamlit
* 🖼️ Add movie posters using TMDB API
* 📊 Improve recommendation accuracy
* 🔎 Add search suggestions/autocomplete

---

## 👩‍💻 Author

**Kalyani**
AI & ML Student

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!
