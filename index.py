import sys

def main():
    arg = sys.argv[1].lower()

    match arg:
        case "/name": name()

        case "/fact": fact()

        case "/why": why()

        case "/what": what()

        case _: failsafe()



def name():
    print("My name is Jordan Veldkamp")

def why():
    print("I went into computer science because I wanted to learn to write code to make games. ")

def what():
    print("After college I hope to get a job releasing either software tools or video games. ")

def fact():
    print("I use arch linux as my daily driver OS. \n btw.")

def failsafe():
    print("I have no answer for that!")




if __name__ == "__main__":
    main()