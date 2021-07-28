import random 
import sys
import time
import os
import re
import json
import webbrowser

from urllib.request import Request, urlopen

def intro():
    time.sleep(1)
    print('  _   _ _         __      ___ _                ')
    print(' | \ | (_)        \ \    / (_) |               ')
    print(' |  \| |_ _ __ _   \ \  / / _| |__   ___  ___  ')
    print(" | . ` | | '__| | | \ \/ / | | '_ \ / _ \/ __| ")
    print(' | |\  | | |  | |_| |\  /  | | |_) |  __/\__ \ ')
    print(' |_| \_|_|_|   \__,_| \/   |_|_.__/ \___||___/ ')
    print('                                               ')
    time.sleep(1)
    print("   _____ _             _ _        ")
    print("  / ____| |           | (_)       ")
    print(" | (___ | |_ _   _  __| |_  ___   ")
    print("  \___ \| __| | | |/ _` | |/ _ \ ")
    print("  ____) | |_| |_| | (_| | | (_) | ")
    print(" |_____/ \__|\__,_|\__,_|_|\___/  ")
    print("                                  ")

    time.sleep(1)
    os.system('cls')

def hangmangamepog():
    #Just in case there is an error
    def errorhandler():
        print('We have run into an unexpected error, Restarting your game')
        hangmanstart()

    #This is the start of the game
    def hangmanstart():
        #Acssii art of the word Hangman because its cool
        print('  _    _              _   _    _____   __  __              _   _ ')
        print(' | |  | |     /\     | \ | |  / ____| |  \/  |     /\     | \ | |')
        print(' | |__| |    /  \    |  \| | | |  __  | \  / |    /  \    |  \| |')
        print(' |  __  |   / /\ \   | . ` | | | |_ | | |\/| |   / /\ \   | . ` |')
        print(' | |  | |  / ____ \  | |\  | | |__| | | |  | |  / ____ \  | |\  |')
        print(' |_|  |_| /_/    \_\ |_| \_|  \_____| |_|  |_| /_/    \_\ |_| \_|')
        print('                                                                 ')
        time.sleep(1)
        print('Welcome to hangman') #welcome
        time.sleep(0.1) 
        hangmaninitiate = 1 
        #asking for how many players
        while hangmaninitiate:
            playerno = input('Enter 1 for 1 player or enter 2 for 2 player: ')
            if playerno == '1' or playerno == '2':
                hangmaninitiate -= 1
            else:
                print('Please answer with the correct input!')
                time.sleep(0.1)
                playerno = input('Enter 1 for 1 player or enter 2 for 2 player: ')
        if playerno == '1': #if 1 start player1
            player_1()
        else: #if 2 start player2
            player_2()
            
    def player_1(): #code for single player
        word_list = []
        with open('words.txt', 'r') as file: #opens the file with the words
            for line in file:
                line = line.strip() #removes spaces in the list
                word_list.append(line) #adds all the words to the list
        word = random.choice(word_list) #gets a random word from the list
        hangman(word) #starts the hangman function with the randomly chosen word

    def player_2():
        word = input('Player 1, what is the word you want player 2 to guess?: ') #requests a word from player 1 to give to player 2
        word = word.lower()
        for i in range(20): #spam out the chat so player 2 cannot see the word
            time.sleep(0.1)
            print("| This is to clear the chat so player 2 can't see the word")
        hangman(word) #starts the hangman function with the given word

    #hangman game    
    def hangman(word):
        blanks = '_'*len(word) #creates the amount of underscores
        blanks_list = list(blanks) #list of the underscores
        tester_blanks_list = list(blanks)
        word_list = list(word) #creates a list with the word
        guesses = 0 #sets the amount of letter guessed to 0
        guess_list = [] #sets the guessed letter list to nothing
        hangman_images(word, guesses) #start the hangman images function
        print(' '.join(blanks_list)) #prints the underscores
        time.sleep(0.1)
        while guesses < 8: #allows them to guess
            guess = input('Guess a letter: ') #requests a letter
            time.sleep(0.1) 
            guess = guess.lower() #lowers the guess so that it doesnt matter if it is capital
            if guess == ' ': #does not allow ' ' as an input
                print('You cannot guess this')
                time.sleep(0.1)
            elif len(guess) != 1: #makes it so you can only input 1 letter
                print('Please only type in 1 valid letter')
                time.sleep(0.1)
            elif guess in guess_list: #stops them from guessing th same letter twice
                print('You have already guessed this letter')
                time.sleep(0.1)
                guesses_print = ' '.join(guess_list) #takes all the guessed letters and makes them a string
                print(f'You have guessed the following letters: {guesses_print}') #prints out the guessed letters
                time.sleep(0.1)
            elif guess in word_list: #if the guessed letter is one of the letters
                i = 0
                while i < len(word):
                    if guess == word[i]:
                        tester_blanks_list[i] = guess
                    i = i + 1
                if tester_blanks_list == blanks_list:
                    print('Incorrect')
                    time.sleep(0.1)
                    print(f'You have {8-guesses} guesses remaining')
                    time.sleep(0.1)
                    hangman_images(guesses, word) #creates the image for the guess
                    if guesses < 8: #if the number of guesses taken is less than 8
                        print('Guess again')
                        time.sleep(0.1)
                        print(' '.join(blanks_list)) #print out a string of letters and underscores
                elif word_list != blanks_list:
                    blanks_list = tester_blanks_list[:]
                    print(' '.join(blanks_list)) #prints out the correctly guessed letters
                    if word_list == blanks_list: #checks if the list of letters in the word is the same as the guessed letters
                        print('You win!')
                        time.sleep(0.1)
                        again = input('Press p to play again, Press any other character to quit: ') #asks if they want to play again
                        if again == 'p': #checks if they pressed p, if so play again
                            hangmanstart() #starts the game again
                        sys.exit()
                    else: #if they get the letter right
                        print('Good job. Guess Again!')
                    
                
            else:
                guess_list.append(guess) #adds the incorrect guess to the list of guesses taken
                print('Incorrect you lose 1 guess')
                time.sleep(0.1)
                guesses = guesses + 1 #adds one to the number of guesses taken
                print(f'You have {8 - guesses} guesses remaining') #prints how many gueses remaining
                hangman_images(guesses, word) #creates a hangman image with remaining guesses
                
    def hangman_images(guesses, word): # prints the corresponding image for each of the guesses
        if guesses == 0:
            print('|')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
        if guesses == 1:
            print(' ___________')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
        elif guesses == 2:
            print(' ___________')
            time.sleep(0.1)
            print('|         |')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
        elif guesses == 3:
            print(' ___________')
            time.sleep(0.1)
            print('|         |')
            time.sleep(0.1)
            print('|         O')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
        elif guesses == 4:
            print(' ___________')
            time.sleep(0.1)
            print('|         |')
            time.sleep(0.1)
            print('|         O')
            time.sleep(0.1)
            print('|         |')
            time.sleep(0.1)
            print('|         |')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
        elif guesses == 5:
            print(' ___________')
            time.sleep(0.1)
            print('|         |')
            time.sleep(0.1)
            print('|         O')
            time.sleep(0.1)
            print('|         |/')
            time.sleep(0.1)
            print('|         |')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
        elif guesses == 6:
            print(' ___________')
            time.sleep(0.1)
            print('|         |')
            time.sleep(0.1)
            print('|         O')
            time.sleep(0.1)
            print('|        \|/')
            time.sleep(0.1)
            print('|         |')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print('|')
        elif guesses == 7:
            print(' ___________')
            time.sleep(0.1)
            print('|         |')
            time.sleep(0.1)
            print('|         O')
            time.sleep(0.1)
            print('|        \|/')
            time.sleep(0.1)
            print('|         |')
            time.sleep(0.1)
            print('|         \ ')
            time.sleep(0.1)
            print('|')
        elif guesses == 8:
            print(' ___________')
            time.sleep(0.1)
            print('|         |')
            time.sleep(0.1)
            print('|         O')
            time.sleep(0.1)
            print('|        \|/')
            time.sleep(0.1)
            print('|         |')
            time.sleep(0.1)
            print('|        /\ ')
            time.sleep(0.1)
            print('|')
            time.sleep(0.1)
            print(f'You have lost!\nThe word was {word}')
            time.sleep(0.1)
            play_again = input('press p to play again, press any other key to quit: ') #To play again
            if play_again == 'p': #If one is pressed, the game will start again
                hangmanstart()
            else:
                print('Thanks for playing!!')
                print('Made by niruvibes')
                website = input('Before this closes, wanna go to my website? (y/n): ')
                if website == 'y' or website == 'yes':
                    webbrowser.open("https://niruvibes.github.io/", new=1)
                    exit()
                else:
                    exit() 

    hangmanstart()

def rockpaperscissors():
    def sprstart(): 
        #Acssii art of the word Hangman because its cool
        print('   _____ _____  _____  ')
        print('  / ____|  __ \|  __ \ ')
        print(' | (___ | |__) | |__) |')
        print('  \___ \|  ___/|  _  / ')
        print('  ____) | |    | | \ \ ')
        print(' |_____/|_|    |_|  \_\ ')
        print('                       ')
        time.sleep(1)
        print('Welcome to scissors paper rock') #welcome
        time.sleep(0.1) 
    playerscore = 0
    compscore = 0
    sprstart()
    while True:
        print(f"\nP {playerscore} - {compscore} C")
        time.sleep(0.5)
        if compscore == 3:
            time.sleep(1)
            os.system('cls')
            print('lmaooo u suck')
            playerscore = 0
            compscore = 0
            time.sleep(2)
            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                print('Thanks for playing!!')
                print('Made by niruvibes')
                website = input('Before this closes, wanna go to my website? (y/n): ')
                if website == 'y' or website == 'yes':
                    webbrowser.open("https://niruvibes.github.io/", new=1)
                    exit()
                else:
                    exit()
        elif playerscore == 3:
            time.sleep(1)
            os.system('cls')
            print('wow so good, you won')
            playerscore = 0
            compscore = 0
            time.sleep(2)
            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                print('Thanks for playing!!')
                print('Made by niruvibes')
                website = input('Before this closes, wanna go to my website? (y/n): ')
                if website == 'y' or website == 'yes':
                    webbrowser.open("https://niruvibes.github.io/", new=1)
                    exit()
                else:
                    exit()
        else: 
            user_action = input("Enter a choice (rock, paper, scissors): ")
            possible_actions = ["rock", "paper", "scissors"]
            computer_action = random.choice(possible_actions)
            print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
            time.sleep(0.5)
            if user_action == computer_action:
                print(f"Both players selected {user_action}. It's a tie!")
            elif user_action == "rock":
                if computer_action == "scissors":
                    print("Rock smashes scissors! You win!")
                    playerscore = playerscore + 1
                elif computer_action == "paper":
                    print("Paper covers rock! You lose.")
                    compscore = compscore + 1
                else:
                    print("Please choose a valid choice")
            elif user_action == "paper":
                if computer_action == "rock":
                    print("Paper covers rock! You win!")
                    playerscore = playerscore + 1
                elif computer_action == "scissors":
                    print("Scissors cuts paper! You lose.")
                    compscore = compscore + 1
                else:
                    print("Please choose a valid option")
            elif user_action == "scissors":
                if computer_action == "paper":
                    print("Scissors cuts paper! You win!")
                    playerscore = playerscore + 1
                elif computer_action == "rock":
                    print("Rock smashes scissors! You lose.")
                    compscore = compscore + 1
                else:
                    print("Please choose a valid choice")

intro()
gameinitiate = 1
while gameinitiate:
    game = input('Do you want to play spr (scissors paper rock) or hangman?: ')
    if game == 'spr' or game == 'hangman':
        gameinitiate -= 1
    else:
        print('Please answer with the correct input! (spr or hangman)')
        time.sleep(0.1)
        game = input('Do you want to play spr (scissors paper rock) or hangman?: ')
if game == 'spr' or game == 'rock': #if spr start rockpaperscissors
    os.system('cls')
    rockpaperscissors()
elif game == 'hangman': #if hangman start hangman
    os.system('cls')
    hangmangamepog()
else:
    os.system('cls')
    print('dm me on discord how tf did u break it this bad, go to my website and click the discord button, https://niruvibes.github.io/')

    
            