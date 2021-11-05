import data

money = 0.00
stop = False
cost = 0.00


def is_not_sufficient(check):
    if data.MENU[check]["ingredients"]["water"] > data.resources["water"]:
        return "Sorry there is not enough water."
    elif data.MENU[check]["ingredients"]["milk"] > data.resources["milk"]:
        return "Sorry there is not enough milk."
    elif data.MENU[check]["ingredients"]["coffee"] > data.resources["coffee"]:
        return "Sorry there is not enough coffee."


def money_check(total):
    if total - cost > 0:
        return True
    else:
        return False


def is_sufficient(check):
    global cost
    cost = data.MENU[check]["cost"]
    if data.MENU[check]["ingredients"]["water"] > data.resources["water"]:
        return False
    if check != "espresso" and data.MENU[check]["ingredients"]["milk"] > data.resources["milk"]:
        return False
    if data.MENU[check]["ingredients"]["coffee"] > data.resources["coffee"]:
        return False
    return True


def report_func():
    water = data.resources["water"]
    milk = data.resources["milk"]
    coffee = data.resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def make_coffee(check):
    data.resources["water"] -= data.MENU[check]["ingredients"]["water"]
    if check != "espresso":
        data.resources["milk"] -= data.MENU[check]["ingredients"]["milk"]
    data.resources["coffee"] -= data.MENU[check]["ingredients"]["coffee"]


while stop is not True:
    inp = input("What would you like? (espresso $1.50/latte $2.50/cappuccino $3.00): ")
    if inp == "report":
        report_func()
    elif inp == "off":
        stop = True
        break
    elif inp == "espresso" or inp == "latte" or inp == "cappuccino":
        if is_sufficient(inp):
            print("Please insert coins.")
            money_input = 0.00
            money_input += 0.25 * int(input("How many quarters?: "))
            money_input += 0.10 * int(input("How many dimes?: "))
            money_input += 0.05 * int(input("How many nickels?: "))
            money_input += 0.01 * int(input("How many cents?: "))
            if money_check(money_input):
                change = money_input - cost
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                print(f"Enjoy your {inp} ☕️. Enjoy!")
                make_coffee(inp)
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(is_not_sufficient(inp))

    else:
        print("Wrong option selected.")