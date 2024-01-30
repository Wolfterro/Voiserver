import io
import socketserver
import soundfile

from src.audio import VoiserverAudio


class UDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def __init__(self, request, client_address, server, **kwargs):
        self.content = []
        super().__init__(request, client_address, server)

    def handle(self):
        self.content.append(self.request[0])
        # data = open("Rapaz2.wav", "rb")

        print(len(self.content), self.content)
        voiserver_audio = VoiserverAudio()
        voiserver_audio.play(content=self.content)
        print(len(self.content))
        print("")
