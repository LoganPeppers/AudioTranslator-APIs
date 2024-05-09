from dotenv import load_dotenv
from libretranslatepy import LibreTranslateAPI
import json, os
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)
import firstDraft
from firstDraft import Ui_MainWindow
from ibm_watson import TextToSpeechV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Includes the API calls needed for each operation.
load_dotenv()
__package__='apiCalls'

#Path to the audio file
audioFile = Ui_MainWindow.fileName
transcription = ""
translatedText = ""
translatedAudio = ""
keyDG = "" 
keyIBM = ""

def getKeys(path):
    global keyDG
    global keyIBM 
    keyFile = open(path, 'r')
    keys = keyFile.read()
    tokens = keys.split("\n")
    keyDG = tokens[0]
    keyIBM = tokens[1]


#DG Transcribe Local File
def transcribe():
    try:
        #Create a Deepgram client using the API key
        getKeys("C:/Users/peppe/OneDrive/Desktop/keys.txt")
        deepgram = DeepgramClient(keyDG)   
        #Open the file chosen through the gui
        with open(audioFile, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        #STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="whisper-tiny",
            smart_format=True,
            
        )

        # STEP 3: Call the transcribe_file method with the text payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options, timeout=300)
        #The response is a lot of jumbled json data. The indexing gets the actual sentence transcribed.
        bTranscription = json.loads(response.to_json(indent=4))['results']['channels'][0]['alternatives'][0]['transcript']
        print(response.to_json(indent=4))
        print(bTranscription)
        #STEP 4: Start up the local LT API and send it the text to translate
        lt = LibreTranslateAPI("http://localhost:5000")
        transcription = lt.translate(bTranscription, "en", "es")
        print(transcription)
        
        #STEP 5: Hand that translation to IBM's TTS service, currently translating from english to spanish
        authenticator = IAMAuthenticator(keyIBM)
        text_to_speech = TextToSpeechV1(authenticator=authenticator)
        text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com')
        with open('hello_world.mp3', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                transcription,
                voice='es-ES_EnriqueV3Voice',
                accept='audio/mp3'        
            ).get_result().content)
        
        
        Ui_MainWindow.resultsPopUp(bTranscription, transcription, os.path.dirname(os.path.abspath(firstDraft)))

    except Exception as e:
        print(f"Exception: {e}")
  


