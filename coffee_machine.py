report={
    "Water":{"amount" : 300 , "unit" :"ml"},
    "Milk": {"amount" : 200 , "unit" : "ml"},
    "Coffee":{"amount" : 100, "unit" : "ml"},
    "Money":{"amount" : 0 , "unit" : "$"}
}

money={
    "quarter":0.25,
    "dimes":0.10,
    "nickles":0.05,
    "pennies":0.01
}

moneylist=["quarter","dimes","nickles","pennies"]

def espresso():
    total=0
    
    if report["Milk"]["amount"]>=30 and report["Water"]["amount"]>=10 and report["Coffee"]["amount"]>=7:
        
        for x in moneylist:
            moninput=int(input(f"Enter {x} "))
            total += moninput * money[x]
        print(f"${total:.2f}")
        if total<3:
            print("Not enough money.")
            tryagain=input("Do you want to try again? y/n: ")
            if tryagain=="y":
                return True
            else:
                return False
        if total>3:
            change=total-3
            print(f"here is your change: {change:.2f}")
            report["Water"]["amount"]-=10
            report["Milk"]["amount"]-=30
            report["Coffee"]["amount"]-=7
            report["Money"]["amount"]+=3
            print("Enjoy your coffee!!!")
            tryagain=input("Do you want anything else? y/n: ")
            return True if tryagain=="y" else False
        else:
            report["Water"]["amount"]-=10
            report["Milk"]["amount"]-=30
            report["Coffee"]["amount"]-=7
            report["Money"]["amount"]+=3
            print("Enjoy your coffee!!!")
            tryagain=input("Do you want anything else? y/n: ")
            return True if tryagain=="y" else False
            
    else:
        print("Not enough resources.")

def cappucino():
    total=0
    
    if report["Milk"]["amount"]>=10 and report["Water"]["amount"]>=10 and report["Coffee"]["amount"]>=15:
        
        for x in moneylist:
            moninput=int(input(f"Enter {x} "))
            total += moninput * money[x]
        print(f"${total:.2f}")
        if total<7:
            print("Not enough money.")
            tryagain=input("Do you want to try again? y/n: ")
            if tryagain=="y":
                return True
            else:
                return False
        if total>7:
            change=total-7
            print(f"here is your change: {change:.2f}")
            print("Here's your coffee...ENJOY!!!")
            report["Water"]["amount"]-=10
            report["Milk"]["amount"]-=10
            report["Coffee"]["amount"]-=15
            report["Money"]["amount"]+=7
            print("Enjoy your coffee!!!")
            tryagain=input("Do you want anything else? y/n: ")
            return True if tryagain=="y" else False

        else:

            print("Here's your coffee...ENJOY!!!")
            report["Water"]["amount"]-=10
            report["Milk"]["amount"]-=10
            report["Coffee"]["amount"]-=15
            report["Money"]["amount"]+=7
            print("Enjoy your coffee!!!")
            tryagain=input("Do you want anything else? y/n: ")
            return True if tryagain=="y" else False
    else:
        print("Not enough resources.")

def latte():
    total=0
    
    if report["Milk"]["amount"]>=40 and report["Water"]["amount"]>=5 and report["Coffee"]["amount"]>=5:
        
        for x in moneylist:
            moninput=int(input(f"Enter {x} "))
            total += moninput * money[x]
        print(f"${total:.2f}")
        if total<4:
            print("Not enough money.")
            tryagain=input("Do you want to try again? y/n: ")
            if tryagain=="y":
                return True
            else:
                return False
        if total>4:
            change=total-4
            print(f"here is your change: {change:.2f}")
            report["Water"]["amount"]-=5
            report["Milk"]["amount"]-=40
            report["Coffee"]["amount"]-=5
            report["Money"]["amount"]+=4
            print("Enjoy your coffee!!!")
            tryagain=input("Do you want anything else? y/n: ")
            return True if tryagain=="y" else False
        else:
            print("Here's your coffee...ENJOY!!!")
            report["Water"]["amount"]-=5
            report["Milk"]["amount"]-=40
            report["Coffee"]["amount"]-=5
            report["Money"]["amount"]+=4
            print("Enjoy your coffee!!!")
            tryagain=input("Do you want anything else? y/n: ")
            return True if tryagain=="y" else False
    else:
        print("Not enough resources.")


tryagain=True
while tryagain==True:    
    x=input("What do you want? espresso/latte/cappucino: ")
    if x=="espresso":
        tryagain=espresso()
    elif x=="latte":
        tryagain=latte()
    elif x=="cappucino":
        tryagain=cappucino()
    elif x == "report":
        print("Current Report")
        for item, detail in report.items():
            print(f"{item}:{detail["amount"]} {detail["unit"]}")
        print("--------------------------\n")
        tryagain = True
    else:
        print("You typed wrong word. Try again.")
        tryagain=True