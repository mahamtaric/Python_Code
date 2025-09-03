import random
def mode(gamemode):
    if gamemode=="easy":
        return 11
    if gamemode=="hard":
        return 6     
num=random.randint(1,100)
print("welcome to number guessing game!")
print("im thinking of a no between 1 and 100. You can GUESS!!!")
gamemode=input("choose a difficulty level: 'easy' or 'hard'? ")
x=mode(gamemode)
lives=x-1
print(f"you have {x-1} attempts to guess")
for i in range(1,x):
    
    guess=int(input("make guess: "))
    if guess>num:
        print("too high,guess again.")
        lives-=1
        print(f"you have {lives} left")
    if guess<num:
        print("too low,guess again. ")
        lives-=1
        print(f"you have {lives} left")
    if guess==num:
        print("CORRECT GUESS QUEEN, YOU WONNNNN!!!")
        exit()
    if lives==0:
        print("Game over 0 lives left")
        exit()