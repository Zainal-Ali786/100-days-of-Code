from main import MENU, resources


def format_data(drink, ingredient):
    return MENU[drink]["ingredients"][ingredient]

def total_paid():
    print("Please insert coins.")
    quarter = int(input("how many quarters?: "))
    dime = int(input("how many dimes?: "))
    nickle = int(input("how many nickels?: "))
    penny = int(input("how many pennies?: "))

    return (quarter*.25) + (dime*.10) + (nickle*.05) + (penny*.01)

def make_coffee(drink, cost, paid):
    change = str(round(paid - cost, 2))
    return "Here is your $"+ change +" in change.\n"+ "Here is your " + drink +". Enjoy!"


def vending():
    total_water = resources["water"]
    total_milk = resources["milk"]
    total_coffee = resources["coffee"]
    total_money = 0
    stop_vending = False


    while not stop_vending:
        #prompt user for what kind of drink
        water = "water"
        milk = "milk"
        coffee = "coffee"
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        if drink == "off":
            stop_vending = True
        elif drink == "report":
            print(f"Water: {total_water}ml")
            print(f"Milk: {total_milk}ml")
            print(f"Coffee: {total_coffee}g")
            print(f"Money: ${total_money}")
        else:
            water = format_data(drink, water)
            milk = format_data(drink, milk)
            coffee = format_data(drink, coffee)


            #TODO: 2. Turn off coffee machine by entering 'off' to the prompt

            #TODO: 3. Print Report


            #TODO: 4. Check resources sufficient
            if total_water < water:
                print("Sorry there is not enough water")
            elif total_milk < milk:
                print("Sorry there is not enough milk")
            elif total_coffee < coffee:
                print("Sorry there is not enough coffee")
            else:

            #TODO: 6. Check transaction successful?
                total_water -= water
                total_milk -= milk
                total_coffee -= coffee
                paid = total_paid()

                cost = MENU[drink]["cost"]
                if cost > paid:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    total_money += cost
                    print(make_coffee(drink, cost, paid))




    #TODO 7. Make Coffee


vending()