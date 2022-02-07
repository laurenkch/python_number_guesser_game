from random import randint

play = True

while (play == True):


    gameplay = input ("If you'd like to guess the number this round, press any key. If you'd like to the computer to guess your number, press 'X' ")

    if (gameplay == 'X'):
        game = True

        while (game == True):
            number = input("Pick a number between 1 and 10. ")
            number = int(number)

            if (number > 10) or (number < 1):
                print("Invalid number. Number must be between 1 and 10")
                continue
            
            isGuessing = True
            low = 1
            high = 10

            while (isGuessing == True):
                guess = randint(low, high)

                if (guess == number):
                    print("The computer guessed your number ", guess, ". Game over.", sep = '')
                    break
                if (guess > number):
                    print("The computer guessed", guess, ". Too high.", sep = '')
                    high = guess - 1
                else:
                    print("The computer guessed", guess, ". Too low.", sep = '')
                    low = guess + 1
        
            isGuessing = False
            game = False

    else:
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
                    print ("Too high.")
                else:
                    print("Too low. ")

                play = play - 1
            
                if (play == 0):
                    print("No guesses remaining. You lose :( ")
                    break
                else:
                    print("Guess again")

            game = False

    reply = input("Play again? Press any key to continue. Press 'X' to exit. ")

    if (reply == "X"):
        play = False
    else:
        play = True
        continue