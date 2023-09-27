from .audio_source import AudioSource

class MP3AudioSource(AudioSource):
    """Audio source from file .mp3"""

    def __init__(self, mp3_path: str):
        super().__init__(self)
        self.mp3_path = mp3_path

    def fourier(self):
        pass
