def display_menu():
    print("Welcome to the Shopping Cart Program!\n"
          "Please select one of the following:\n"
          "1. Add item\n"
          "2. View cart\n"
          "3. Remove item\n"
          "4. Compute total\n"
          "5. Quit")


def add_item(names, prices):
    item_name = input("What item would you like to add? ")
    item_price = float(input(f"What is the price of '{item_name}'? $"))
    names.append(item_name)
    prices.append(item_price)
    print(f"'{item_name}' has been added to the cart.")


def view_cart(names, prices):
    print("The contents of the shopping cart are:")
    for i, (name, price) in enumerate(zip(names, prices), start=1):
        print(f"{i}. {name} - ${price:.2f}")


def remove_item(names, prices):
    try:
        item_number = int(input("Which item would you like to remove? ")) - 1
        if 0 <= item_number < len(names):
            removed_name = names.pop(item_number)
            removed_price = prices.pop(item_number)
            print(f"{removed_name} - ${removed_price:.2f} removed.")
        else:
            print("Sorry, that is not a valid item number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def compute_total(prices):
    total = sum(prices)
    print(f"The total price of the items in the shopping cart is ${total:.2f}")


def shopping_cart():
    names = []
    prices = []

    while True:
        display_menu()
        choice = input("Please enter an action: ")

        if choice == '1':
            add_item(names, prices)
        elif choice == '2':
            view_cart(names, prices)
        elif choice == '3':
            remove_item(names, prices)
        elif choice == '4':
            compute_total(prices)
        elif choice == '5':
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


shopping_cart()