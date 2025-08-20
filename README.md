# 🍲 NutriSnap AI

**Your Personalized Nutritionist Powered by Google Gemini**

NutriSnap AI is an AI-powered nutrition assistant built with **Streamlit** and **Google Gemini API**.
It analyzes uploaded food images and provides:

* ✅ Dish Name & Ingredients
* ✅ Step-by-step Cooking Instructions
* ✅ Nutritional Value Breakdown
* ✅ Alternative Dishes with Similar Nutrition

Supports **English** & **Hindi** for a personalized experience! 🌐

---

## 🚀 Features  

- 📤 Upload an image of any dish (JPG, JPEG, PNG).  
- 🧠 AI-powered analysis using **Gemini 1.5 Flash**.  
- 🍽️ Get dish name, origin & ingredients.  
- 👨‍🍳 Learn how to cook step-by-step.  
- 📊 Get detailed nutritional insights in tabular format for dishes **or any food/product**.  
- 🥗 Get vegetarian & non-vegetarian alternatives.  
- 🌐 Supports **English** and **Hindi**.  


---

## 🛠️ Tech Stack

* **Streamlit** – UI framework
* **Google Generative AI (Gemini)** – AI-powered responses
* **Pillow (PIL)** – Image processing

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/NutriSnap-AI.git
cd NutriSnap-AI
```

2. **Create a virtual environment** (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up your API key**

* Create a `.env` file in the root directory
* Add your Google API key inside it:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Upload a food image 🍛 and start exploring nutrition insights!

---

## 📂 Project Structure

```
NutriSnap-AI/
│-- app.py                 # Main Streamlit app
│-- requirements.txt       # Dependencies
│-- .env                   # API Key (not pushed to GitHub)
│-- README.md              # Project Documentation
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues and pull requests.

---

## 📜 License

This project is licensed under the **MIT License**.

---

---
👨‍💻 Developed by **Avirat Sharma**
