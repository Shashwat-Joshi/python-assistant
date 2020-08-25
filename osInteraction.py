import os
import pyttsx3
import datetime
import time
import random

# Data
guide = "Hi I am Python Assistant, as the name suggests made with ❤ in Python\n1. Can open basic applications on your " \
        "device like chrome, notepad or Vscode" \
        "\n2. Google search (use command search)" \
        "\n3. Tell you current Date and time" \
        "\n4. Rest is a suspense for you to explore my power"

sorryText = ["I don't understand",
             "I'm sorry I didn't got that !",
             "Sorry I didn't get that"]

byeByeText = [
    "See you later alligator",
    "Bye Bye Honey Pie",
    "See ya later"
]

print('Welcome! This is a python assistant')
pyttsx3.speak('Welcome! This is a python assistant')

print('What is your name? - ', end="")
pyttsx3.speak('What is your name?')
name = input()

firstTimeExecution = True
while True:
    print('How can I help you : ', end='')
    if firstTimeExecution:
        pyttsx3.speak(f'Hello {name} How can I help you')
        firstTimeExecution = False

    userInput = input()
    userInput = userInput.lower()

    if 'do not' in userInput or 'not' in userInput or 'dont' in userInput or 'don\'t' in userInput:
        print('Ok I won\'t do that')
        pyttsx3.speak('Ok! I won\'t do that')
    # Logic to exit console
    elif 'exit' in userInput or 'leave' in userInput:
        print('Are you sure you want to exit (Y/N) : ', end='')
        pyttsx3.speak(f'Are you sure you want to exit {name}')
        exitAnswer = input()
        if exitAnswer.lower() == 'y':
            print(f'Exiting console, See you later {name}')
            pyttsx3.speak(f'Exiting console, See you later {name}')
            break

    # Logic for user interaction
    elif 'hi' in userInput or 'hello' in userInput:
        print(f'Hello {name}:)')
        pyttsx3.speak(f'Hello {name}')
    elif 'hey' in userInput:
        print(f'Hi {name}, How you doing ?')
        pyttsx3.speak(f'Hi {name}, How you doing ?')

    # Logic for What you can do or Help
    elif 'help' in userInput or 'can you do' in userInput or 'who are you' in userInput or 'what are you capable' in userInput:
        print(guide)
        pyttsx3.speak(f'This is what I can do {name}')

    # Opening applications
    elif 'execute' in userInput or 'open' in userInput or 'start' in userInput or 'fire' in userInput:
        if 'chrome' in userInput or 'browser' in userInput:
            pyttsx3.speak('opening chrome')
            os.system('chrome')
        elif 'notepad' in userInput:
            pyttsx3.speak('opening notepad')
            os.system('notepad')
        elif 'vscode' in userInput or 'code' in userInput:
            os.system('code')

    # Logic for search
    elif 'search' in userInput:
        print('What would you like to search ? - ', end="")
        pyttsx3.speak('What would you like to search ?')
        searchInput = input()
        if searchInput[-3:] == 'com':
            url = searchInput
        else:
            url = f'https://www.google.com/search?q={searchInput}'
            print(f'Searching for {searchInput}')
            pyttsx3.speak(f'Searching for {searchInput}')
            os.system(f'chrome {url}')

    # Get current Date
    elif 'date' in userInput:
        print(f'The current date is {datetime.date.today()}')
        pyttsx3.speak(f'The current date is {datetime.date.today()}')

    # Get current Time
    elif 'time' in userInput:
        t = time.localtime()
        print(f'Current time is {time.strftime("%H:%M:%S", t)}')
        pyttsx3.speak(f'Current time is {time.strftime("%H:%M:%S", t)}')

    # Logic for bye, take care
    elif 'bye' in userInput:
        randomText = f"{byeByeText[random.randint(0, 2)]}"
        print(randomText)
        pyttsx3.speak(randomText)

    # Sorry Logic
    else:
        randomText = f"{sorryText[random.randint(0, 2)]}"
        print(randomText)
        pyttsx3.speak(randomText)
