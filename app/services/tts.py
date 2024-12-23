import wave

from piper.voice import PiperVoice


class TTSService:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.voice = PiperVoice(model_path)

    def generate_audio(self, text: str):
        temp_wav_file = wave.open("output.wav", "w")
        audio = self.voice.synthesize(text, temp_wav_file)
        temp_wav_file.close()
        # TODO return the base64 audio here

    @staticmethod
    def preprocess_text(text: str):
        pass

    def __call__(self, *args, **kwargs):
        pass
