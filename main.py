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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns can true when order can be made and false if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is no enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("please insert coins...")
    total = int(input("How many quaters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total
def make_coffe(drink_name, order_ingredients):
    """Deduct the ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")
def is_transaction_successfull(money_received, drink_cost):
    """Return True when payment is accepted or false money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change ")
        global  profit
        profit += drink_cost
        return  True
    else:
        print("Sorry thats not enough money, Money refunded.")
        return  False


is_on = True
while is_on:
    choice = input("what would you like? (espresso/latte/cappucino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"Water: {resources['water']}ml")
       print(f"Milk: {resources['milk']}ml")
       print(f"Coffee: {resources['coffee']}g")
       print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successfull(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])





