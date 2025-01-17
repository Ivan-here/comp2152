import random
def number_gussing_game():
    targetNumber = random.randint(1, 100)

    play = input("Do you want to play number gussing gmae? (yes/no)").strip().lower()

    attemps = 0
    max_attemps = 10

    while attemps < max_attemps:
        try:
            userGuess = int(input("Enter your guess: "))
            #attemps = attemps + 1
            attemps += 1
            if userGuess < targetNumber:
                if abs(userGuess - targetNumber) <= 5:
                    print("Too low! You're very close! Try again.")
                else:
                    print("Too low, try again.")    
            elif userGuess > targetNumber:
                if abs(userGuess - targetNumber) <= 5:
                    print("Too High! You're very close! Try again.")
                                        

            return True
        except:
            print("")
    play = input()
    return True
