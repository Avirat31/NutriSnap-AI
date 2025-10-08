from dotenv import load_dotenv
load_dotenv()  
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to call Gemini API
def get_gemini_response(input_prompt, images, user_prompt):
    model = genai.GenerativeModel('gemini-2.0-flash-001')

    # Build input parts: [prompt, image1, image2, ..., user_prompt]
    inputs = [input_prompt]
    inputs.extend(images)
    if user_prompt.strip():
        inputs.append(user_prompt)

    response = model.generate_content(inputs)
    return response.text

# Function to prepare uploaded images
def input_image_setup(uploaded_files):
    image_parts = []
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            image_parts.append({
                "mime_type": uploaded_file.type,
                "data": bytes_data
            })
    return image_parts

# Streamlit app
def main():
    st.set_page_config(page_title="NutriSnap AI 🍲", page_icon="🍲")
    st.markdown("<h1 style='text-align: center; color: #F4A261;'>NutriSnap AI 🍲</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Your Personalized Nutritionist 🤖</h4>", unsafe_allow_html=True)
    st.divider()

    # Language selector
    language_options = ["English", "Hindi"]
    selected_language = st.selectbox("🌐 Select Language:", language_options)

    # Define prompts
    if selected_language == "English":
        input_prompts = {
             "Get Dish Name and Ingredients": """Embark on a culinary exploration as you uncover the secrets of the delectable dish captured in the uploaded image:
        1. Discover key details about the dish, including its name and culinary essence.
        2. Explore the fascinating origins of the dish, unraveling its cultural and historical significance.
        3. Dive into the rich tapestry of ingredients, presented pointwise, that contribute to the dish's exquisite flavor profile.""",
            
            "How to Cook": """As the culinary maestro guiding eager chefs, lay out the meticulous steps for crafting the featured dish:
        1. Start with selecting the finest ingredients, emphasizing quality and freshness.
        2. Detail the process of washing, peeling, and chopping each ingredient with precision.
        3. Unveil the culinary artistry behind the cooking process, step by step.
        4. Share expert tips and techniques to elevate the dish from ordinary to extraordinary.""",
            
            "Nutritional Value": """In your role as a nutritional advisor, present a comprehensive overview of the dish's nutritional value:
        1. Display a table showcasing nutritional values in descending order, covering calories, protein, fat, and carbohydrates.
        2. Create a second table illustrating the nutritional contribution of each ingredient, unraveling the dietary secrets within.
        3. **Health rating**:
            - Give a clear score like ⭐⭐⭐⭐☆ (4/5 Healthy).
        4. **Suitability**:
            - Whether it’s good for weight loss, diabetes, bodybuilding, general wellness, etc.""",
            
            "Alternative Dishes with Similar Nutritional Values": """Act as a dietitian and nutritionist:
        1. Your task is to provide 2 vegeterian dish alternative to the dish uploaded in the image which have the same nutritional value.
        2. Your task is to provide 2 Non-vegeterian dish alternative to the dish uploaded in the image which have the same nutritional value."""
        }
    else:
        input_prompts = {
            "Get Dish Name & Ingredients": """उपयुक्त छवि में कैद किए गए स्वादिष्ट व्यंजन ...""",
            "How to Cook": """उत्सुक शेफ्स को मार्गदर्शन करने वाले ...""",
            "Nutritional Value": """एक पोषण विशेषज्ञ के रूप में इस व्यंजन का विश्लेषण करें और बताएं:

1. **प्रति सर्विंग कैलोरी विभाजन**:
   - कुल कैलोरी
   - प्रोटीन (ग्राम, %)
   - कार्ब्स (ग्राम, %)
   - फैट्स (ग्राम, %)

2. **स्वास्थ्य प्रोफ़ाइल**:
   - यह हाई-प्रोटीन, लो-कार्ब, वेगन-फ्रेंडली, कीटो आदि है या नहीं।
   - संतुलित है या नहीं।

3. **स्वास्थ्य रेटिंग**:
   - ⭐⭐⭐⭐☆ (4/5 हेल्दी) जैसी स्पष्ट रेटिंग दें।

4. **उपयुक्तता**:
   - क्या यह वज़न घटाने, डायबिटीज़, बॉडीबिल्डिंग या सामान्य स्वास्थ्य के लिए अच्छा है।""",
            "Alternative Dishes": """एक रसोई समाचार पत्र के रूप में ..."""
        }

    # File uploader for multiple images
    uploaded_files = st.file_uploader("📤 Upload one or more dish images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if uploaded_files:
        st.image([Image.open(f) for f in uploaded_files], caption=[f.name for f in uploaded_files], use_column_width=True)

    st.divider()

    # Extra user prompt
    user_prompt = st.text_input("📝 Add your own extra prompt (optional):")

    # Buttons for actions
    st.markdown("### ✨ Choose an Action:")
    col1, col2 = st.columns(2)

    with col1:
        btn1 = st.button("🍽️ Get Dish Name & Ingredients")
        btn2 = st.button("👨‍🍳 How to Cook")
    with col2:
        btn3 = st.button("📊 Nutritional Value")
        btn4 = st.button("🥗 Alternative Dishes")

    # Handle button clicks
    for label, clicked in zip(input_prompts.keys(), [btn1, btn2, btn3, btn4]):
        if clicked:
            if uploaded_files:
                with st.spinner("🔍 Analyzing the dish..."):
                    img_parts = input_image_setup(uploaded_files)
                    response = get_gemini_response(input_prompts[label], img_parts, user_prompt)
                    st.success("✅ Output:")
                    st.markdown(f"### {label}")
                    st.write(response)
            else:
                st.error("⚠️ Please upload at least one image.")

if __name__ == "__main__":
    main()
