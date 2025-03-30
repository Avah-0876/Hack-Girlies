from flask import Flask, request, jsonify, render_template
import google.generativeai as genai 

# initialize the name of the website. we know that our webpage is based in this file here
app = Flask(__name__)

def processor(characters, era):
    """
    """
    # pong specific processor
    if(characters == "Pong"):
        prompt = '''Write funny fanfic, interweaving juicy, compelling tropes from the perspective of the ball from Pong 
        (the original arcade versions). Make it set in the 60s and subtly incorporate 1-3 words of terminology/ slang from that era. 
        250 words max. At the beginning of the fanfic, write a funny title. Make sure the story has a beginning, middle, and end.'''

    # space race specific processor
    if(characters == "Space Race"):
        prompt = '''Write a story, interweaving juicy, compelling tropes from the perspective of one of the ships in the early 
        combat arcade game Space Race (the game - not the Cold War event) . Make it set in the 60s and subtly incorporate 1-3 words of 
        terminology/slang from that era. 250 words max. At the beginning of the fanfic, write a funny title. Be careful NOT to mix it up 
        with other games like Space Invaders - Space Race was a distinct game.'''

    # computer space specific processor
    if(characters == "Computer Space"):
        prompt = ''' Write a [type] story, interweaving juicy, compelling tropes from the perspective of one of the ships in the early combat 
        arcade game Computer Space (the game that evolved from SpaceWar! but was popularly played by the public). Make it set in the 60s and 
        subtly incorporate 1-3 words of terminology/slang from that era. 250 words max. At the beginning of the fanfic, write a funny title. 
        Be careful NOT to mix it up with other games like Space Invaders - Computer Space was a distinct game").'''
    
    # everything else. GENERAL PROMPT
    else:  
        prompt = f'''Write fanfic, interweaving juicy, compelling tropes about characters from {characters} (the original arcade versions).
            Make sure it is set in the {era} and very subtly incorporate 1-3 words of terminology/ slang from that era. 250 words max. 
            At the beginning of the fanfic, write a funny title. Make sure the story has a beginning, middle, and end.'''
    
    #for c in characters:
      #  prompt += c 
    #prompt = prompt + 'set in the' + era
    
    #API key
    genai.configure(api_key="AIzaSyAGYW8CZPOtnEtYP_DsC9x35xhSBOLB4ew")

    #Establishing model
    model = genai.GenerativeModel("gemini-1.5-flash")

    #Producing response
    response = model.generate_content(prompt)

    return response.text

# now, establish a link to our entry html file
@app.route("/")
def home():
    return render_template("era1.html")

@app.route("/api", methods=["POST"])
def api():
    data = request.get_json()  # Get JSON data from the request
    characters = data.get('characters', "")  
    timeperiod = data.get('timeperiod', "")    
    
    if not characters or not timeperiod:
        return jsonify({'error': 'Missing characters or era'}), 400
    
    
    result = processor(characters, timeperiod)
    return jsonify({'response': result})


# making sure this runs
if __name__ == "__main__":
    app.run(debug = True)