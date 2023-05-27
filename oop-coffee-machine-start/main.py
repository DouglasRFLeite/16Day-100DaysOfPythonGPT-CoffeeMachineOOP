from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while True:
        command = input(f"What would you like? ({menu.get_items()})")

        if command == "off":
            break

        if command == "report":
            coffee_maker.report()
            money_machine.report()
            continue

        drink_wanted = menu.find_drink(command)
        if not coffee_maker.is_resource_sufficient(drink_wanted):
            break

        if not money_machine.make_payment(drink_wanted.cost):
            break

        coffee_maker.make_coffee(drink_wanted)

if __name__ == "__main__":
    main()

        