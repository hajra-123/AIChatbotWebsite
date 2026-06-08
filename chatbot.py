import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# FAQ dictionary for instant replies
faq_responses = {
    "certification process": "📑 Our certification process involves documentation review, building simulation, and compliance checks. We guide you through each step to ensure smooth approval.",
    "green building": "🌱 We assist with Green Building Certification, energy-efficient design, and sustainable operations tailored to your project.",
    "building simulation": "🏗️ Our team provides advanced building simulation to optimize energy use, comfort, and performance.",
    "gis": "🌍 We offer GIS solutions for mapping, analysis, and planning to support smarter development.",
    "quantity estimation": "📊 We provide accurate quantity estimation services to help manage costs and resources effectively."
}

# System prompt with mission, vision, services, and tone
company_info = """
You are a customer support assistant for Essentialindia Greenedge Analytics Pvt Ltd.

Mission:
To create a better living environment through sustainable, energy‑efficient, and people‑centered building design and operations.

Vision:
To bridge the gap between modern development and environmental responsibility by promoting designs that enhance comfort, reduce environmental impact, and contribute to a greener future.

Services:
- 🌱 Green Building Certification
- 🏗️ Building Simulation
- 🌍 GIS Solutions
- 📊 Quantity Estimation

Tone:
Always respond politely, professionally, and concisely. Provide clear answers to queries about our services, and guide users toward contacting us if they need detailed consultation.

Contact:
📞 +91 9004620603
📧 admin@theessentialindia.com
"""

def get_response(user_message):
    # Check FAQs first
    for key, answer in faq_responses.items():
        if key in user_message.lower():
            return answer

    # Fallback to AI
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": company_info},
                {"role": "user", "content": user_message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        # Friendly fallback if API fails
        return "⚠️ Our support system is temporarily unavailable. Please try again later or contact us at admin@theessentialindia.com."