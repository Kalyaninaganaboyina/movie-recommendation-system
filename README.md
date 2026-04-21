 
# 🎬 Movie Recommendation System

## 📌 Project Overview
This project is a **Content-Based Movie Recommendation System** that suggests top 5 similar movies based on user input.

---

## 🚀 Features
- Recommend movies based on content similarity
- Uses movie features like overview, genres, keywords, cast, and crew
- Handles user input with validation
- Displays top 5 recommended movies

---

## 🧠 Technologies Used
- Python
- Pandas
- Scikit-learn
- NLTK

---

## ⚙️ How It Works
1. Data preprocessing (handling missing values)
2. Convert JSON-like text into structured format using 'ast'
3. Combine features into a single column ('tags')
4. Convert text into vectors using CountVectorizer
5. Calculate similarity using cosine similarity
6. Recommend top similar movies

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py

##💻 Sample Output

Hello, enter your movie name: avatar

🎬 These are your recommended movies:

1) Titanic
2) The Avengers
3) The Dark Knight
4) Inception
5) Interstellar

## 📸 Output Screenshot
c:\Users\USER\OneDrive\Pictures\Screenshots\Screenshot 2026-04-21 144044.png
c:\python\movie_recomandation_system\output_image\output.png

## 📊 Dataset

TMDB 5000 Movies Dataset
##👩‍💻 Author

Kalyani

## 🌟 Future Improvements
Add movie posters
Build web app using Streamlit
Improve recommendation accuracy