import random
cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]
def calculate_total(hand):
    total = sum(hand)
    if 1 in hand and total <= 11:
        total += 10
    return total
def shuffshuff():

    card1=random.choice(cards)
    card2=random.choice(cards)
    listofcards=[card1,card2]
    return listofcards
def hit():
    
    card3=random.choice(cards)
    return card3

total=0
dealertotal=0
ans1=input("do you want to play blackjack? y/n: ")
if ans1=="y":
    yours=shuffshuff()
    print(yours)
    print(sum(yours))

    dealers=shuffshuff()
    print(f"{dealers[0]},_____(hidden)")
    dealertotal=calculate_total(dealers)


    choice1=input("do you want to hit or stand? ")
    while choice1=="hit":
        anothercard=hit()
        yours.append(anothercard)
        print(yours)
        total=calculate_total(yours)
        
        print(total)
        
        if total>21:
            print("It is a bust!!! Dealer WON")
            exit()
        choice1=input("do you want to hit or stand? ")

    if choice1=="stand":
       
        total=calculate_total(yours)
        print(total)


        while dealertotal<17:
            dealercard3=hit()
            dealers.append(dealercard3)
            dealertotal=calculate_total(dealers)
        
        print(dealers)
        print(dealertotal)

        if total == 21:
            print("Blackjack! You win!")
            exit()
        if dealertotal == 21:
            print("Dealer has Blackjack! You lose!")
            exit()
        if dealertotal>21:
           print("It is a bust!!! YOU WON")
           exit()
        if 1 in yours and total<=11:
           total+=10
        if total > dealertotal:
           print("You win!")
        elif total < dealertotal:
           print("Dealer wins!")
        else:
           print("It's a tie!")