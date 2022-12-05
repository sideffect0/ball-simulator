from ballsimulator import game
from okgoogle import recognizer

if __name__ == '__main__':
    print("""
     Please enter your option number
     1. BallSimulator
     2. Speech Recognition
    """)
    option = int(input())

    if option == 1:
        game.start()
    elif option == 2:
        recognizer.recognize()

