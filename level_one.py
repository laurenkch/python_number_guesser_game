from random import randint

game = True

while (game == True):
    number = randint(1,10)
    play = 3

    while (play > 0):

        if (play > 1):
            print("You have", play, "guesses remaining.")
        else:
            print("You have", play, "guess remaining.")
        guess = input("Pick a number between 1 and 10. ")
        guess = int(guess)
        
        if (guess > 10 ) or (guess < 1):
            print("Invalid. Number must be between 1 and 10. ")
            continue

        if (guess == number):
            print("You win! The number was", number, )
            break
        elif (guess > number):
            print ("Too high. Guess again ")
        else:
            print("Too low. Guess again ")

        play = play - 1
    
        if (play == 0):
            print("No guesses remaining. You lose :( ")
    
    reply = input ("Press any key to play again. Press 'X' to exit ")

    if (reply == 'X'):
        game = False
    else:
        continue



