# Name: Rusho Binnabi
# Date: 5/10/2024
# Project: Text to Speech
# Contact Information: RushoBinnabi123@yahoo.com

# this text to speech program turns the text entered using either the keyboard or from a text file into speech.

from gtts import gTTS
import sys
import time
from os import system, name

# this state variable will be used to switch between the different states for the functionality for the program.
state = 0
state = int(state)

# this text() function takes input from the keyboard and turns it into speech.
# @param input this input is the text being entered from the keyboard.
# @param name the name of the output file 
def text(input, name):
    try:
        data = input
        textToSpeech = gTTS(text=data, lang='en', slow=False)
        textToSpeech.save(name)
        print("Phrase saved!")
        print("")
    except:
        print("Error. Please enter a phrase.")
        print("")

# this exitProgram() function exits the program.
def exitProgram():
    print("Goodbye!")
    sleepFor2Seconds()
    clearScreen()
    sys.exit()

# this clearScreen() function clears the screen.
def clearScreen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

# this sleepFor2Seconds() function slows down the execution of the program by 2 seconds.
def sleepFor2Seconds():
    time.sleep(2)    

# this file() function reads from a file and turns it into speech.
# @param input the name of the file being read.
# @param name the name of the output file.
def file(input, name):
    try:
        with open (input, "r") as file:
            data = file.readlines()
        fileText = ""
        fileText = fileText.join(data)
        textToSpeech = gTTS(text=fileText, lang='en', slow=False)
        textToSpeech.save(name)
        print("File Saved!")
        print("")
    except:
        print("Error. Please enter a filename.")
        print("")

# this while statement block is the implemented state machine that will change functions based on user specifications and is where the program starts from.
while state == 0: # state 0 is where the program starts from. It will always loop back to state 0 if the user wants to keep using it.
    userInput = input("Would you like to use the text-to-speech with a file or keyboard (f/k) (press n to exit)?: ")
    print("")
    if userInput == "f":
        state = 1
    elif userInput == "k":
        state = 2
    elif userInput == "n":
        print("")
        clearScreen()
        exitProgram()
    if state == 1: # state 1 is if the user wants to use the program with a file.
        fileName = str(input("Enter the filename to save the phrase to: "))
        print("")
        fileName = fileName + ".mp3"
        phrase = str(input("Enter the filename to read from: "))
        print("")
        phrase = phrase + ".txt"
        file(phrase, fileName)
        sleepFor2Seconds()
        print("")
        clearScreen()
        repeat = input("Would you like to use the program again (y/n)?: ")
        print("")
        if repeat == "y":
            state = 0
            clearScreen()
            sleepFor2Seconds()
        elif repeat == "n":
            print("")
            clearScreen()
            exitProgram()
    elif state == 2: # state 2 is if the user wants to use the keyboard for the program.
        fileName = str(input("Enter the filename to save the phrase to: "))
        print("")
        fileName = fileName + ".mp3"
        phrase = str(input("Enter the phrase: "))
        print("")
        text(phrase, fileName)
        sleepFor2Seconds()
        clearScreen()
        repeat = str(input("Would you like to use the program again (y/n)?: "))
        print("")
        if repeat == "y":
            state = 0
            clearScreen()
            sleepFor2Seconds()
        elif repeat == "n":
            print("")
            clearScreen()
            exitProgram()