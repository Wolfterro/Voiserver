import pyaudio
import wave
import io
from threading import Thread


class VoiserverAudio(object):
    def __init__(self):
        # PyAudio config
        self.chunk = 1024
        self.format = pyaudio.paFloat32
        self.channels = 1
        self.rate = 44100

    def play(self, content):
        audio = pyaudio.PyAudio()

        stream = audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            output=True,
            frames_per_buffer=self.chunk,
        )

        stream.write(content.pop(0), self.chunk)
        stream.close()

        # play = Thread(target=VoiserverAudio.thread_play_frames, args=(content, stream, self.chunk, ))
        # play.setDaemon(True)
        # play.start()
        # play.join()

    # Static Methods
    # --------------
    @staticmethod
    def thread_play_frames(content, stream, chunk):
        stream.write(content.pop(0), chunk)
        stream.close()