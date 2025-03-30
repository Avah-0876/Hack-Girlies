#importing libraries
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai 

app = Flask(__name__)

def cross(era):
    """
    """
    return []

def chars(character, era_lst):
    """
    """
    if character not in era_lst:
        era_lst.append(character)
    return era_lst

#Gemini AI Function
def processor(characters, era):
    """
    """
    prompt = 'give me a 250 word story about '
    for c in characters:
        prompt += c 
    prompt = prompt + 'set in the' + era
    
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
    characters = data.get('characters', [])  # Expecting a list of characters
    era = data.get('era', '')               # Expecting a string

    if not characters or not era:
        return jsonify({'error': 'Missing characters or era'}), 400

    result = processor(characters, era)
    return jsonify({'response': result})

if __name__ == '__main__':
    app.run(debug=True)
