This personal project is experimenting with stitching together APIs to accomplish a larger goal. I utilize Deepgram's Whisper Speech-To-Text model to transcribe an audio file, hand that text to LibreTranslate's localhost API to translate into a different language, and use IBM Cloud's Text-To-Speech API Service to dictate those results into .mp3 format. The tool is as accurate as free-tier API keys can get you. I'm not complaining though, the ease of implementing such a wide variety of technologies fascinates me!

The first step is booting up the LibreTranslate self-hosted server. Doing this automatically is a work in progress.
Running the program brings up a UI with three buttons: upload file, submit, and cancel.
The flow is supposed to go: 1. Hit upload file and choose the audio to be translated. 2. Hit submit. 
The hello_world.mp3 file is then generated in the root directory with the last translated audio. 


Future Features:
-submit and cancel greyed out until file is chosen.
-choose input and output languages
-choose where to save output file
-LibreTranslate instance run at start of program
-transcription/file name displayed in gui
