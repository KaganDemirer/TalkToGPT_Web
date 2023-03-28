import talkToGPT
import tts
import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listen', methods=['GET'])
def listen():
    prompt = talkToGPT.recordAndSend()
    return {'prompt': prompt}

@app.route('/chat', methods=['POST'])
def chat():
    data = list(request.form.items())[0][0]
    prompt = json.loads(data)['prompt']
    response = talkToGPT.chatgpt.chat(prompt)
    return {'response': response}

@app.route('/speak', methods=['POST'])
def speak():
    data = list(request.form.items())[0][0]
    prompt = json.loads(data)['prompt']
    response = talkToGPT.talk(prompt)
    return {'response': response}

if __name__ == '__main__':
    tts.initialize_speech_synthesizer()
    talkToGPT.chatgpt.system("Du wurdest so eingestellt, dass du reden kannst. Drücke dich menschlich, kurz und prägnant aus. Deine Antwort gibst du immer in der Sprache, welche die prompt des Users ist.")
    app.run()