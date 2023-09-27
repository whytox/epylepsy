from abc import ABC

class Representation(ABC):
    """Audio source representation after a certain analysis.
    It encapsulates the parameters and the value of the
    audio source analysis which will be used by the visualization.
    This is how the machine represent the audio source,
    it could be a FFT with different number of bins and other parameters."""
    pass