import pandas as pd
class Transaction:
    """
    Represents a transaction management system.

    Attributes:
        data (dict): A dictionary containing the transaction data, including item names, quantities, prices, and total prices.
        id_trx (int): The ID of the transaction.

    Methods:
        get_transaction_id(): Prompts the user for a transaction ID and returns it.
        start(): Starts the transaction management system and allows the user to choose various functions.
        display_functions(): Displays the available functions.
        add_item(): Adds an item to the transaction.
        update_item_name(): Updates the name of an existing item in the transaction.
        update_item_qty(): Updates the quantity of an existing item in the transaction.
        update_item_price(): Updates the price of an existing item in the transaction.
        delete_item(): Deletes an item from the transaction.
        reset_transaction(): Resets the transaction data.
        check_order(): Checks the order for null values in the transaction data.
        display_data(): Displays the transaction data in a tabular format.
        total_price(): Calculates the total price and applicable discount for the transaction.
    """

    def __init__(self):
        """
        Initializes a new Transaction2 object.

        Summary:
            Displays the program title and initializes the transaction data and ID.

        Attributes:
            data (dict): A dictionary to store the transaction data.
            id_trx (int): The ID of the transaction.
        """
        print('===Super Cashier===')
        self.data = {"Item": [], "Qty": [], "Price": [], "Total Price": []}
        self.id_trx = self.get_transaction_id()

    def get_transaction_id(self):
        """
        Prompts the user for a transaction ID and returns it.

        Summary:
            Allows the user to input a transaction ID and validates it as an integer.

        Parameters:
            None

        Return:
            int: The validated transaction ID entered by the user.
        """
        while True:
            try:
                id_trx = int(input('Input transaction ID: '))
                print(f'Your transaction ID: {id_trx}\n')
                return id_trx
            except ValueError:
                print('Numbers only!')

    def start(self):
        """
        Starts the transaction management system and allows the user to choose various functions.

        Summary:
            Displays the available functions and prompts the user for a function selection.
            Executes the selected function based on user input.

        Parameters:
            None

        Return:
            None
        """
        while True:
            self.display_functions()
            chosen_funct = int(input('\nSelect a function (write number): '))

            if chosen_funct == 1:
                print("\n=== Add Items ===")
                self.add_item()
            elif chosen_funct == 2:
                print("\n=== Update Item Name ===")
                self.update_item_name()
            elif chosen_funct == 3:
                print("\n=== Update Item Quantity ===")
                self.update_item_qty()
            elif chosen_funct == 4:
                print("\n=== Update Item Price ===")
                self.update_item_price()
            elif chosen_funct == 5:
                print("\n=== Delete Items ===")
                self.delete_item()
            elif chosen_funct == 6:
                print("\n=== Clear Transaction Data ===")
                self.reset_transaction()
            elif chosen_funct == 7:
                print("\n=== Check Order ===")
                self.check_order()
            elif chosen_funct == 8:
                print("\n=== Checkout/Pay Now ===")
                self.total_price()
            else:
                print("\nFunction unavailable")
                
            continue_choice = input("\nBack to main menu? (y/n) ").lower()
            if continue_choice == 'n':
                break

    def display_functions(self):
        """
        Displays the available functions.

        Summary:
            Prints a list of available functions for the user to choose from.

        Parameters:
            None

        Return:
            None
        """
        print('\nFunctions List:')
        print('1. Add items')
        print('2. Update item name')
        print('3. Update item quantity')
        print('4. Update item price')
        print('5. Delete items')
        print('6. Clear transaction data')
        print('7. Check order')
        print('8. Checkout/Pay now')


    def add_item(self):
        """
        Adds an item to the transaction.

        Summary:
            Prompts the user for item details (name, quantity, and price) and updates the transaction data accordingly.
            Displays the updated transaction data after adding the item.

        Parameters:
            None

        Return:
            None
        """
        while True:
            item_name = input('\nItem (type "done" to finish adding items): ')
            if item_name == "done":
                break
            while True:
                try:
                    item_qty = int(input('Item Quantity: '))
                    item_price = int(input('Price: '))
                    break
                except ValueError:
                    print('Numbers only are allowed')

            self.data["Item"].append(item_name)
            self.data["Qty"].append(item_qty)
            self.data["Price"].append(item_price)
            self.data["Total Price"].append(item_price * item_qty)
            self.display_data()

    def update_item_name(self):
        """
        Updates the name of an existing item in the transaction.

        Summary:
            Prompts the user for the current item name and the new item name, and updates the transaction data accordingly.
            Displays the updated transaction data after modifying the item name.

        Parameters:
            None

        Return:
            None
        """
        old_name = input("Enter the current item name to be modified: ")
        if old_name not in self.data["Item"]:
            print("Item not found")
            return

        new_name = input("Enter the new item name: ")
        name_index = self.data["Item"].index(old_name)
        self.data["Item"][name_index] = new_name
        print(f'Successfully changed item name from {old_name} to {new_name}\n')
        self.display_data()

    def update_item_qty(self):
        """
        Updates the quantity of an existing item in the transaction.

        Summary:
            Prompts the user for the current item name and the new quantity, and updates the transaction data accordingly.
            Displays the updated transaction data after modifying the item quantity.

        Parameters:
            None

        Return:
            None
        """
        old_name = input("Enter the current item name to be modified: ")
        if old_name not in self.data["Item"]:
            print("Item not found")
            return

        new_qty = int(input(f"Enter the new quantity for {old_name}: "))
        name_index = self.data["Item"].index(old_name)
        self.data["Qty"][name_index] = new_qty
        print(f'Successfully changed {old_name} quantity to {new_qty}\n')
        self.display_data()

    def update_item_price(self):
        """
        Updates the price of an existing item in the transaction.

        Summary:
            Prompts the user for the current item name and the new price, and updates the transaction data accordingly.
            Displays the updated transaction data after modifying the item price.

        Parameters:
            None

        Return:
            None
        """
        old_name = input("Enter the current item name to be modified: ")
        if old_name not in self.data["Item"]:
            print("Item not found")
            return

        new_price = int(input(f"Enter the new price for {old_name}: "))
        name_index = self.data["Item"].index(old_name)
        self.data["Price"][name_index] = new_price
        print(f'Successfully changed {old_name} price to {new_price}\n')
        self.display_data()

    def delete_item(self):
        """
        Deletes an item from the transaction.

        Summary:
            Prompts the user for the item name and removes the corresponding entry from the transaction data.
            Displays the updated transaction data after removing the item.

        Parameters:
            None

        Return:
            None
        """
        item_name = input("Enter which item to remove: ")
        if item_name in self.data["Item"]:
            index = self.data["Item"].index(item_name)
            for key in self.data:
                self.data[key].pop(index)
            print("Item removed successfully.\n")
        else:
            print("Item not found in the dictionary.\n")
        self.display_data()

    def reset_transaction(self):
        """
        Resets the transaction data.

        Summary:
            Clears all values stored in the transaction data, effectively resetting the transaction.
            Displays the empty transaction data after resetting.

        Parameters:
            None

        Return:
            None
        """
        for key in self.data:
            self.data[key].clear()
        print("Transaction reset successfully.\n")
        self.display_data()

    def check_order(self):
        """
        Checks the order for null values in the transaction data.

        Summary:
            Identifies any null values (empty cells) in the transaction data and prompts the user to update them if found.
            Displays the transaction data and the list of null values if any.

        Parameters:
            None

        Return:
            None
        """
        null_values = []
        for key, values in self.data.items():
            for i, value in enumerate(values):
                if not value:
                    null_values.append((key, i))

        if null_values:
            print("Null values found in the table:")
            for key, index in null_values:
                print(f"- Key: {key}, Index: {index}")
            print("Please update the table!\nUpdate the table one-by-one. The function will search the null values vertically. Same column first.\n")
        else:
            print("No null values found in the dictionary.\n")
        self.display_data()

    def display_data(self):
        """
        Displays the transaction data.

        Summary:
            Prints the transaction data in a tabular format.

        Parameters:
            None

        Return:
            None
        """
        print("==== My Basket ====")
        df = pd.DataFrame(self.data)
        print(df)
        print("====" * (len(df.columns) + 1))

    def total_price(self):
        """
        Calculates the total price and applicable discount for the transaction.

        Summary:
            Calculates the total price of all items in the transaction and applies a discount based on the total amount spent.
            Prints the total price, discount amount, and the final amount to pay.

        Parameters:
            None

        Return:
            None
        """
        self.display_data() #display transaction data
        total_before_disc = sum(self.data["Total Price"])
        total_after_disc = 0
        disc = 0

        if total_before_disc > 500_000:
            disc = 0.1
            total_after_disc = total_before_disc - (total_before_disc * disc)
            print(f"Congratulations! You just got a 10% discount for spending more than Rp 500,000")
        elif total_before_disc > 300_000:
            disc = 0.08
            total_after_disc = total_before_disc - (total_before_disc * disc)
            print(f"Congratulations! You just got an 8% discount for spending more than Rp 300,000")
        elif total_before_disc > 200_000:
            disc = 0.05
            total_after_disc = total_before_disc - (total_before_disc * disc)
            print(f"Congratulations! You just got a 5% discount for spending more than Rp 200,000")
        else:
            total_after_disc = total_before_disc

        print(f"Total price: \t{total_before_disc}")
        print(f"Discount: \t{disc* 100}%")
        print(f"Amount to pay: \t{total_after_disc}")