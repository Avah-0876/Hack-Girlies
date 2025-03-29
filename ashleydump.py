from google import genai

client = genai.Client(api_key="AIzaSyAGYW8CZPOtnEtYP_DsC9x35xhSBOLB4ew")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Tell me a bedtime story!",
)

print(response.text)