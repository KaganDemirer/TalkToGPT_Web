import openai
import datetime
import stt
import tts
import chatgpt

openai.api_key = "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"
dt = datetime.datetime.now()
chatgpt = chatgpt.ChatGPT()

def recordAndSend():
    prompt = stt.recognize_from_mic()
    try:
        if prompt.strip() == "":
            print("No text found")
            return
        return prompt
    except:
        print("No text found")
        return
    
def talk(text):
    tts.save_text_to_speech(text)