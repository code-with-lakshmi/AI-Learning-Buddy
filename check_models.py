import google.generativeai as genai

genai.configure(api_key="AIzaSyDkNfmcYk2Ha_Mkm_eOjCVgNlSywwgUZd4")

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)