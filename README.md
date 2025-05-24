# 🎬 Movie Recommendation System

Built with **Python**, **Streamlit**, and powered by the **OMDb API**, this app recomends movies including its posters.

---

## 🧠 Motivation

In an age where content is abundant and user attention is scarce, recommending the right movie can enhance user experience dramatically. This project aims to:

- Help users **find interesting movies** based on their favorite titles.
- Serve as a demo project to showcase how **external APIs**, **environment variables**, and **Streamlit** can be integrated into a Python application.
- Provide a foundation for more advanced recommendation engines in the future using ML/AI techniques.

---

## 🚀 Features

- 🔎 **Search by Title**: Enter a movie name to get recommendations.
- 🧾 **Movie Info**: Get the movie and poster.
- 📽️ **Recommendations**: Get similar or related movies (basic logic or future placeholder for advanced ML).
- 🌐 **Data**: Uses [OMDb API](http://www.omdbapi.com/) to fetch fresh movie data.
- 🧪 **Clean & Minimal UI**: Built using Streamlit for rapid and beautiful front-end development.

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** – For building the interactive UI
- **Requests** – For sending HTTP requests to OMDb API
- **dotenv** – For securely managing API keys
- **OMDb API** – Source of real-time movie data

---

## 📂 Project Structure

```bash
movie-recommendation-app/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # List of Python dependencies
├── .env                  # Your OMDb API key (excluded from Git)
├── .env.example          # Template for your env file
├── .gitignore            # Files to be ignored by Git
└── README.md             # Project documentation
