import google as genai

client = genai.Client(api_key="AIzaSyAGYW8CZPOtnEtYP_DsC9x35xhSBOLB4ew")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)