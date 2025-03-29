#importing libraries
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai 

app = Flask(__name__)

#Gemini AI Function
def processor(prompt):
    """
    """
    prompt = prompt + 'story that is 250 words long'
    #API key
    genai.configure(api_key="AIzaSyAGYW8CZPOtnEtYP_DsC9x35xhSBOLB4ew")

    #Establishing model
    model = genai.GenerativeModel("gemini-1.5-flash")

    #Producing response
    response = model.generate_content(prompt)

    return response.text

@app.route('/')
def index():
    return render_template('test_web.html') 

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()  # Get JSON data from the request
    prompt = data.get('text')  # Extract the text
    if not prompt:
        return jsonify({'error': 'No text provided'}), 400
    result = processor(prompt)
    return jsonify({'response': result})

if __name__ == '__main__':
    app.run(debug=True)
