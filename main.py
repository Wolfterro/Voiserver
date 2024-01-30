from src.server import VoiserverServer


def main():
    server = VoiserverServer()
    server.init()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(">> Closing...")
