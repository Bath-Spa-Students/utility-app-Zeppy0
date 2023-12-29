print('''
╭╮╱╱╭┳━━━┳━╮╱╭┳━━━┳━━┳━╮╱╭┳━━━╮╭━╮╭━┳━━━┳━━━┳╮╱╭┳━━┳━╮╱╭┳━━━╮
┃╰╮╭╯┃╭━━┫┃╰╮┃┣╮╭╮┣┫┣┫┃╰╮┃┃╭━╮┃┃┃╰╯┃┃╭━╮┃╭━╮┃┃╱┃┣┫┣┫┃╰╮┃┃╭━━╯
╰╮┃┃╭┫╰━━┫╭╮╰╯┃┃┃┃┃┃┃┃╭╮╰╯┃┃╱╰╯┃╭╮╭╮┃┃╱┃┃┃╱╰┫╰━╯┃┃┃┃╭╮╰╯┃╰━━╮
╱┃╰╯┃┃╭━━┫┃╰╮┃┃┃┃┃┃┃┃┃╱┃┃┃╭━╮┃┃┃┃┃┃┃╰━╯┃┃╱╭┫╭━╮┃┃┃┃┃╰╮┃┃╭━━╯
╱╰╮╭╯┃╰━━┫┃╱┃┃┣╯╰╯┣┫┣┫┃╱┃┃┃╰┻━┃┃┃┃┃┃┃╭━╮┃╰━╯┃┃╱┃┣┫┣┫┃╱┃┃┃╰━━╮
╱╱╰╯╱╰━━━┻╯╱╰━┻━━━┻━━┻╯╱╰━┻━━━╯╰╯╰╯╰┻╯╱╰┻━━━┻╯╱╰┻━━┻╯╱╰━┻━━━╯''')

class VendingMachine:
    def __init__(self):
        # Define the menu with items, codes, prices, and quantities
        self.menu = {
            '1': {'item': 'Coke', 'price': 2.50, 'quantity': 12},
            '2': {'item': 'Pepsi', 'price': 2.50, 'quantity': 11},
            '3': {'item': 'Fanta', 'price': 2.50, 'quantity': 10},
            '4': {'item': 'KitKat', 'price': 2, 'quantity': 15},
            '5': {'item': 'Twix', 'price': 4, 'quantity': 12},
            '6': {'item': 'Skittles', 'price': 4, 'quantity': 9},
            '7': {'item': 'Water', 'price': 1, 'quantity': 18},
        }
        # Initialize the amount of money
        self.money_in_machine = 0.0

    # Display the menu to the user
    def display_menu(self):
        print("=== Vending Machine Menu ===")
        for code, details in self.menu.items():
            print(f"{code}: {details['item']} - DHS{details['price']:.2f} (Quantity: {details['quantity']})")

    # Take user input for item selection
    def process_selection(self):
        selection = input("Enter the code of the item you want to purchase: ")
        if selection in self.menu and self.menu[selection]['quantity'] > 0:
            item_details = self.menu[selection]
            return item_details
        elif selection not in self.menu:
            print("Invalid selection. Please try again.")
        else:
            print("Sorry, the selected item is out of stock. Please choose another item.")
        return None

    # Take user input for money
    def accept_money(self):
        money_inserted = float(input("Insert money (in DHS): "))
        return money_inserted

    # Dispense the selected item
    def dispense_item(self, item):
        print(f"\nDispensing {item['item']}, Enjoy...!")
        item['quantity'] -= 1

    # Calculate and return the change
    def give_change(self, money_inserted, item_price):
        change = money_inserted - item_price
        print(f"Change: DHS{change:.2f}")
        return change

    def run_vending_machine(self):
        while True:
            self.display_menu()
            selected_item = self.process_selection()

            if selected_item:
                item_price = selected_item['price']
                money_inserted = self.accept_money()

                if money_inserted >= item_price:
                    self.dispense_item(selected_item)
                    change = self.give_change(money_inserted, item_price)
                    self.money_in_machine += item_price
                    self.money_in_machine -= change
                else:
                    print("Insufficient Funds. Transaction Canceled.")

                # Another transaction
                another_transaction = input("Do you want to make another purchase? (yes/no): ").lower()
                if another_transaction == "no":
                    print("Thank you for using the vending machine.")
                    break


# Start the VendingMachine class
vending_machine = VendingMachine()

# Run the code
vending_machine.run_vending_machine()