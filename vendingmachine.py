print('''
╭╮╱╱╭┳━━━┳━╮╱╭┳━━━┳━━┳━╮╱╭┳━━━╮╭━╮╭━┳━━━┳━━━┳╮╱╭┳━━┳━╮╱╭┳━━━╮
┃╰╮╭╯┃╭━━┫┃╰╮┃┣╮╭╮┣┫┣┫┃╰╮┃┃╭━╮┃┃┃╰╯┃┃╭━╮┃╭━╮┃┃╱┃┣┫┣┫┃╰╮┃┃╭━━╯
╰╮┃┃╭┫╰━━┫╭╮╰╯┃┃┃┃┃┃┃┃╭╮╰╯┃┃╱╰╯┃╭╮╭╮┃┃╱┃┃┃╱╰┫╰━╯┃┃┃┃╭╮╰╯┃╰━━╮
╱┃╰╯┃┃╭━━┫┃╰╮┃┃┃┃┃┃┃┃┃╱┃┃┃╭━╮┃┃┃┃┃┃┃╰━╯┃┃╱╭┫╭━╮┃┃┃┃┃╰╮┃┃╭━━╯
╱╰╮╭╯┃╰━━┫┃╱┃┃┣╯╰╯┣┫┣┫┃╱┃┃┃╰┻━┃┃┃┃┃┃┃╭━╮┃╰━╯┃┃╱┃┣┫┣┫┃╱┃┃┃╰━━╮
╱╱╰╯╱╰━━━┻╯╱╰━┻━━━┻━━┻╯╱╰━┻━━━╯╰╯╰╯╰┻╯╱╰┻━━━┻╯╱╰┻━━┻╯╱╰━┻━━━╯''')

class VendingMachine:
    def __init__(self):
        # Define the menu with items, codes and prices
        self.menu = {
            '1': {'item': 'Coke', 'price': 2.50},
            '2': {'item': 'Pepsi', 'price': 2.50},
            '3': {'item': 'Fanta', 'price': 2.50},
            '4': {'item': 'KitKat', 'price': 2},
            '5': {'item': 'Twix', 'price': 4},
            '6': {'item': 'Skittles', 'price': 4},
            '7': {'item': 'Water', 'price': 1},
        }
        # Initialize the amount of money
        self.money_in_machine = 0.0

    # Display the menu to the user
    def display_menu(self):
        print("=== Vending Machine Menu ===")
        for code, details in self.menu.items():
            print(f"{code}: {details['item']} - DHS{details['price']:.2f}")

    # Take user input for item selection
    def process_selection(self):
        selection = input("Enter the code of the item you want to purchase: ")
        if selection in self.menu:
            item_details = self.menu[selection]
            return item_details
        else:
            print("Invalid selection. Please try again.")
            return None

    # Take user input for money
    def accept_money(self):
        money_inserted = float(input("Insert money (in DHS): "))
        return money_inserted

    # Dispense the selected item
    def dispense_item(self, item):
        print(f"\nDispensing {item['item']}, Enjoy...!")

    # Calculate and return the change
    def give_change(self, money_inserted, item_price):
        change = money_inserted - item_price
        print(f"Change: DHS{change:.2f}")
        return change

    def run_vending_machine(self):
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

# Start the VendingMachine class
vending_machine = VendingMachine()

# Run the code
vending_machine.run_vending_machine()
