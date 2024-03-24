This personal project is experimenting with stitching together APIs to accomplish a larger goal. I utilize Deepgram's Whisper Speech-To-Text model to transcribe an audio file, hand that text to LibreTranslate's localhost API to translate into a different language, and use IBM Cloud's Text-To-Speech API Service to dictate those results into .mp3 format. The tool is as accurate as free-tier API keys can get you. I'm not complaining though, the ease of implementing such a wide variety of technologies fascinates me!

The first step is booting up the LibreTranslate self-hosted server. --ssl
