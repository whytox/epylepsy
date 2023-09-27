from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io import wavfile
from tempfile import mktemp


def spectrogram(file, format):
    if format == 'mp3':
        mp3_audio = AudioSegment.from_file(file, format="mp3")  # read mp3
        wname = mktemp('.wav')  # use temporary file
        mp3_audio.export(wname, format="wav")  # convert to wav
        FS, data = wavfile.read(wname)  # read wav file
    elif format == 'wav':
        FS, data = wavfile.read(file)  # read wav file
    else:
        raise ValueError("format not supported")
    plt.specgram(data[:, 0], Fs=FS, NFFT=1024, noverlap=0)  # plot
    plt.show()
    plt.figure()
    plt.specgram(data[:, 0], mode="magnitude", Fs=FS, NFFT=1024, noverlap=0)  # plot
    plt.show()
    plt.figure()
    plt.specgram(data[:, 0], mode="psd", Fs=FS, NFFT=1024, noverlap=0)  # plot
    plt.show()
    plt.figure()
    plt.specgram(data[:, 0], mode="phase", Fs=FS, NFFT=1024, noverlap=0)  # plot
    plt.show()
    plt.figure()
    plt.specgram(data[:, 0], mode="angle", Fs=FS, NFFT=1024, noverlap=0)  # plot
    plt.show()
    return
