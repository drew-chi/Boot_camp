import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

global profit
profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"""
    Water: {resources.get("water")}ml
    Milk: {resources.get("milk")}ml
    Coffee: {resources.get("coffee")}g
    Money: ${format(profit, '.2f')}
""")


def stockcheck(order):
    for item in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][item] > resources[item]:
            print(
                f"Not enough {item} to make this order, please make another selection or refill {item} in the machine!")
            return 0
    return 1


def payment(order):
    global profit
    cost = MENU[order]["cost"]
    total = 0.0
    print(f"The total of the order will be {format(cost, '.2f')}")
    while total < cost:
        print("Insert coins")
        q = int(input("No. of quarters:"))
        total += q * .25
        if total >= cost:
            break
        d = int(input("No. of dimes:"))
        total += d * .1
        if total >= cost:
            break
        n = int(input("No. of nickles:"))
        total += n * .05
        if total >= cost:
            break
        p = int(input("No. of pennies:"))
        total += p * .01
        if total < cost:
            print(f"You are short ${format(round(cost - total, 2), '.2f')}")
            cont = input("Would you like to insert more coins?(yes/no)")
            if cont == "yes":
                pass
            if cont == "no":
                print(f"Returning ${format(round(total, 2), '.2f')}")
                return 0
    profit += cost
    change = float(format(total - cost, '.2f'))
    if round(change) == 0:
        print(f"Thank you! Your {order} will be ready soon!")
    else:
        print(f"Thank you! Your change is ${change}. Your {order} will be ready soon!")


def resourceadj(order):
    for item in resources:
        update = resources[item] - MENU[order]["ingredients"][item]
        resources[item] = update
    time.sleep(3)
    print("Order is ready!")


def refill(w, m, c):
    resources["water"] += int(w)
    resources["milk"] += int(m)
    resources["coffee"] += int(c)
    print("Refill complete! Current status is:")
    report()


def startup():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino):")
        if choice == "report":
            report()
        elif choice == "off":
            break
        elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
            check = stockcheck(choice)
            if check == 0:
                break
            if check == 1:
                if payment(choice) == 0:
                    print("Transaction Cancelled")
                    break
            resourceadj(choice)
        elif choice == "fill":
            water = input("How many ml of water would you like to add?")
            milk = input("How many ml of milk would you like to add?")
            coffee = input("How many grams of coffee would you like to add?")
            if water == "cancel" or milk == "cancel" or coffee == "cancel":
                print("Refill cancelled!")
            refill(water, milk, coffee)
        else:
            print("Invalid entry!")


startup()
