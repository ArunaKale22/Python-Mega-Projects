import os
import google.generativeai as genai

# Configure API key (replace with your actual key)
# genai.configure(api_key="AIzaSyAFCb40p1hJvLRoihkPJ2qHIBICqOQ4X44")  

# def generate():
#     model = genai.GenerativeModel("gemini-1.5-flash")  # Use correct model name

#     response = model.generate_content("Who is Donald trump?")

#     print(response.text)  # Print the AI-generated response

# if __name__ == "__main__":
#     generate()


client = genai.Client(api_key="AIzaSyAFCb40p1hJvLRoihkPJ2qHIBICqOQ4X44")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works"
)
print(response.text)