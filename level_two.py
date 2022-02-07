from random import randint


game = True

while (game == True):
    number = input("Pick a number between 1 and 10 ")
    number = int(number)
    
    if (number > 10) or (number < 1):
        print("Invalid. Number must be between 1 and 10 ")
        continue
    
    play = 0

    while (play < 3):
        guess = randint(1, 10)

        if (guess == number):
            print("Computer guessed your number, ", guess, ". Game over.")
            break
        elif (guess < number):
            print("Computer guessed", guess, ". Too low. ")
        else: 
            print("Computer guessed", guess, ". Too high." )
        
        play = play + 1
    
    if (play == 3):
        print("Computer ran out of guesses. Game over ")
    

    reply = input("Play again? Press any key to continue. Press 'X' to exit")
    if (reply == 'X'):
        game = False
    else:
        continue
    