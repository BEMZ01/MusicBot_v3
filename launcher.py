from bot import MusicBot
import subprocess


def main():
    with open("Lavalink.log", "w+") as log:
        p=subprocess.Popen(['java', '-jar', 'JAVA\\jdk-13.0.2\\bin\\Lavalink.jar'], stdout=log)
    bot = MusicBot()
    bot.run()


if __name__ == "__main__":
    main()
