from abc import ABC

class AudioSource(ABC):
    """Basic audio source class"""

    @abstractmethod
    def fourier(self):
        pass