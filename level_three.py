from random import randint

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
            print("The computer guessed ", guess, ". Too high.", sep = '')
            high = guess - 1
        else:
            print("The computer guessed ", guess, ". Too low.", sep = '')
            low = guess + 1
    
    isGuessing = False


    reply = input("Play again? Press any key to continue. Press 'X' to exit. ")

    if (reply == "X"):
        game = False
    else:
        continue