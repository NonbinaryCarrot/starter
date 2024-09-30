import random
import time

chances = 3
correctguessesleft = 3
blocked = 0
power = True

mixups = ["6K", "2S", "THROW"]


while power == True:

    attempts = 3
    correctguessesleft = 3
    blocked = 0

    if power == False:
        break

    comm = input("> ")

    if comm.lower() == "help":
        print('''

    Hello! Welcome to Millia blocker but it's bullshit!

    Input "start" to start the game.

    input "quit" to close the program.

         ''')

    if comm.lower() == "quit":
        break

    else:
        print("That does not seem to correspond to a command. Please type 'help' for a list of commands")

    if comm.lower() == "start":
        print(f'''
        
    Uh oh! Looks like you lost neutral to pin spam like an idiot!
        
    Millia is about to do her classic neutral on you and now you gotta gamble!
        
    What will it be this time?
        
        ''')

        while attempts > 0 or blocked < 3:

            bullshit = random.choice(mixups)

            guess = input(f'''       
    6K (High) 
            
    2S (Low)
    
    Throw        
    
>''')

            if guess.upper() == bullshit:
                blocked += 1
                correctguessesleft -= 1

                if blocked == 3:
                    print('''

                    waow yuor winndr!!!1!!11

                    you can input start to play again
                    or quit o leave like a dummy
                    ''')
                    break

                if correctguessesleft < 2:
                    print(f"You blocked correctly!!, too bad you gotta guess {correctguessesleft} more time!")
                else:
                    print(f"You blocked correctly!!, too bad you gotta guess {correctguessesleft} more times!")

            if guess.upper() != bullshit:
                attempts -= 1

                if attempts == 0:
                    print('''
                    
                    YOU FUCKING SUCK YOU COULDNT EVEN BLOCK 3 FUCKING MIXUPS????? 
                    GO TRY AGAIN YOU FUCKER
                   
                    TYPE "START" TO TRY AGAIN
                    
                    OR "QUIT" IF YOU GOT A BIG OL FUCKING PUSSY
                    
                    ''')
                    power == False
                    break


                if attempts < 2:
                    print(f'''
                    
                    
        YOU GUESSED WRONG!!!! IT WAS A {bullshit} THERE GOES A THIRD OF YOUR HEALTH!!! THERES {attempts} ATTEMPT LEFT!
                    
                
                    ''')

                else:
                    print(f'''
                    
        YOU GUESSED WRONG!!!! IT WAS A {bullshit} THERE GOES A THIRD OF YOUR HEALTH!!! THERES {attempts} ATTEMPTS LEFT!
                    
                    ''')
