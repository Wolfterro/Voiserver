import socketserver

from src.handler import UDPHandler


class VoiserverServer(object):
    def __init__(self, host='localhost', port=1488):
        self.host = host
        self.port = port

    def init(self):
        self.__start_server()

    # "Private" Methods
    # -----------------
    def __start_server(self):
        print(">> Starting server at {}:{}...".format(self.host, self.port))
        with socketserver.UDPServer((self.host, self.port), UDPHandler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C
            server.serve_forever()
