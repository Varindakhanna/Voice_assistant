#102003291 VARINDA KHANNA 
#102003301 LEEZA
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import sys
import pyjokes
import random
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning minakshi mam!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon minakshi mam!")   

    else:
        speak("Good Evening minakshi mam!")  

    speak("I am voice assistant. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('123varinda.leeza@gmail.com', 'ai_leeza02')
    server.sendmail('varindakhanna2002@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"mam, the time is {strTime}")


        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "varindakhanna2002@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email.please try again") 


        elif 'game' in query:
     


            board = ["-", "-", "-",
                    "-", "-", "-",
                    "-", "-", "-"]
            currentPlayer = "X"
            winner = None
            gameRunning = True

            # game board
            def printBoard(board):
                print(board[0] + " | " + board[1] + " | " + board[2])
                print("---------")
                print(board[3] + " | " + board[4] + " | " + board[5])
                print("---------")
                print(board[6] + " | " + board[7] + " | " + board[8])


            # take player input
            def playerInput(board):
                inp = int(input("Select a spot 1-9: "))
                if board[inp-1] == "-":
                    board[inp-1] = currentPlayer
                else:
                    print("Oops player is already at that spot.")


            # check for win or tie
            def checkHorizontle(board):
                global winner
                if board[0] == board[1] == board[2] and board[0] != "-":
                    winner = board[0]
                    return True
                elif board[3] == board[4] == board[5] and board[3] != "-":
                    winner = board[3]
                    return True
                elif board[6] == board[7] == board[8] and board[6] != "-":
                    winner = board[6]
                    return True

            def checkRow(board):
                global winner
                if board[0] == board[3] == board[6] and board[0] != "-":
                    winner = board[0]
                    return True
                elif board[1] == board[4] == board[7] and board[1] != "-":
                    winner = board[1]
                    return True
                elif board[2] == board[5] == board[8] and board[2] != "-":
                    winner = board[3]
                    return True


            def checkDiag(board):
                global winner
                if board[0] == board[4] == board[8] and board[0] != "-":
                    winner = board[0]
                    return True
                elif board[2] == board[4] == board[6] and board[4] != "-":
                    winner = board[2]
                    return True


            def checkIfWin(board):
                global gameRunning
                if checkHorizontle(board):
                    printBoard(board)
                    print(f"The winner is {winner}!")
                    gameRunning = False

                elif checkRow(board):
                    printBoard(board)
                    print(f"The winner is {winner}!")
                    gameRunning = False

                elif checkDiag(board):
                    printBoard(board)
                    print(f"The winner is {winner}!")
                    gameRunning = False


            def checkIfTie(board):
                global gameRunning
                if "-" not in board:
                    printBoard(board)
                    print("It is a tie!")
                    gameRunning = False


            # switch player
            def switchPlayer():
                global currentPlayer
                if currentPlayer == "X":
                    currentPlayer = "O"
                else:
                    currentPlayer = "X"


            def computer(board):
                while currentPlayer == "O":
                    position = random.randint(0, 8)
                    if board[position] == "-":
                        board[position] = "O"
                        switchPlayer()


            while gameRunning:
                printBoard(board)
                playerInput(board)
                checkIfWin(board)
                checkIfTie(board)
                switchPlayer()
                computer(board)
                checkIfWin(board)
                checkIfTie(board)        

           

        elif 'joke' in query:
            content=pyjokes.get_joke()
            print(content)
            speak(content) 

        elif 'finish' in query:
            print("Thank you have a nice day!! This was the project made by leeza and varinda")
            speak("thank you have a nice day!!")
            speak("This was the project made by leeza and varinda")                       
            sys.exit()   