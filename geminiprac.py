import google.generativeai as genai  # Correct import

# Configure the API key
genai.configure(api_key="AIzaSyAGYW8CZPOtnEtYP_DsC9x35xhSBOLB4ew")  # Replace with your actual API key

# Select a model
model = genai.GenerativeModel("gemini-1.5-flash")  # Use the latest available model

# Generate content
response = model.generate_content("Tell me about a bedtime story in two sentences about a character named Pi")

# Print the response text
print(response.text)
