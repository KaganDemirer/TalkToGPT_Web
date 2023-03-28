import azure.cognitiveservices.speech as speechsdk

# https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=tts

selectedLanguage = "German (Germany)"
selectedLocale = "de-DE"
selectedSpeaker = "AmalaNeural"

def initialize_speech_synthesizer():
    global speech_synthesizer
    speech_key, service_region = "b1c4e8658dd942c3949526f913b3cd58", "westeurope"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_synthesis_voice_name=f"{selectedLocale}-{selectedSpeaker}"
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

def save_text_to_speech(text):
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
