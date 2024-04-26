from dotenv import load_dotenv
from libretranslatepy import LibreTranslateAPI
import os, json, subprocess
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)
from firstDraft import Ui_MainWindow
from ibm_watson import TextToSpeechV1 
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Includes the API calls needed for each operation.
load_dotenv()
__package__='apiCalls'

#DeepGram first:
#Path to the audio file
audioFile = Ui_MainWindow.fileName
transcription = ""
translatedText = ""
translatedAudio = ""

API_KEY_DG = "9fd4fdef42b5772501a69cd6957a71e767eb1ef8"


#DG Transcribe Local File
def transcribe():
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(API_KEY_DG) 
        

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
        #response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options, timeout=300)
        #transcription = json.loads(response.to_json(indent=4))['results']['channels'][0]['alternatives'][0]['transcript']
        # STEP 4: Print the response
        #print(response.to_json(indent=4))
        transcription = "My name is Logan"
        print(transcription)
        #lt = LibreTranslateAPI("http://localhost:5000")
        #print(lt.translate(transcription, "en", "es"))
        
        authenticator = IAMAuthenticator('CyZMRAdIsyzrVR1uU1faeF2Z7Nst4mB-tyqzDr0NTVeS')
        text_to_speech = TextToSpeechV1(authenticator=authenticator)

        text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com')
        with open('hello_world.mp3', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                transcription,
                voice='es-ES_EnriqueV3Voice',
                accept='audio/mp3'        
            ).get_result().content)
        

    except Exception as e:
        print(f"Exception: {e}")

#if __name__ == "__main__":
 #   main()        

#End of DG example code   


