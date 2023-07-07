#modul.py
import pandas as pd

class Transaction:
    # Create a dict to establish a data structure: Item | Qty | Price | Total Price
    data = {"Item": [], "Qty": [], "Price": [], "Total Price": []}

    def __init__(self):
        """
        This is a docstring
        """
        print('===Super Cashier===')
        while True:
            try:
                id_trx = int(input('Input transaction ID: '))
                print(f'Your transaction ID: {id_trx}\n')
                break
            except ValueError:
                print('Numbers only!')
                continue

        while True:
            print('Functions List:')
            print('1. Add items')
            print('2. Update item name')
            print('3. Update item quantity')
            print('4. Update item price')
            print('5. Delete items')
            print('6. Clear transaction data')
            print('7. Check order')
            print('8. Checkout/Pay now')
            chosen_funct = int(input('Select a function (write number): '))

            if chosen_funct == 1:
                print("Starting add_item function...")
                self.add_item()
                
            elif chosen_funct == 2:
                print("Starting update_item_name function...")
                self.update_item_name()
            
            elif chosen_funct == 3:
                print("Starting update_item_qty function...")
                self.update_item_qty()

            elif chosen_funct == 4:
                print("Starting update_item_price function...")
                self.update_item_price()

            elif chosen_funct == 5:
                print("Starting delete_item function...")
                self.delete_item()

            elif chosen_funct == 6:
                print("Starting reset_transaction function...")
                self.reset_transaction()

            elif chosen_funct == 7:
                print("Starting check_order function...")
                self.check_order()

            elif chosen_funct == 8:
                print("Starting total_price function...")
                self.total_price()
                
            else:
                print("Function unavailable")

            continue_choice = input("Continue editing? (y/n) ").lower()
            if continue_choice == 'n':
                break

    def add_item(self):
        """Add an item to the transaction data.

        Asks for item details and appends them to the data dictionary.
        """
        while True:
            item_name = input('Item (type "done" to finish adding items): ').lower()
            if item_name == "done":
                break
            while True:
                try:
                    item_qty = int(input('Item Quantity: '))
                    item_price = int(input('Price: '))
                    break
                # except ValueError:   #to avoid nulls/wrong inputs
                except NameError:
                    print('Numbers only are allowed')

            # Append all newly added items to the dictionary
            self.data["Item"].append(item_name)
            self.data["Qty"].append(item_qty)
            self.data["Price"].append(item_price)
            self.data["Total Price"].append(item_price * item_qty)
            df = pd.DataFrame(self.data)
        print(df)

    def update_item_name(self):
        old_name = input("Enter the current item name to be modified: ").lower()
        if old_name not in self.data["Item"]:
            print("Item not found")
            return

        new_name = input("Enter the new item name: ")
        name_index = self.data["Item"].index(old_name)
        self.data["Item"][name_index] = new_name
        print(f'Successfully changed item name from {old_name} to {new_name}')
        df = pd.DataFrame(self.data)
        print(df)

    def update_item_qty(self):
        old_name = input("Enter the current item name to be modified: ").lower()
        if old_name not in self.data["Item"]:
            print("Item not found")
            return

        new_qty = int(input(f"Enter the new qty for {old_name}: "))
        name_index = self.data["Item"].index(old_name) #find the index of old_name
        self.data["Qty"][name_index] = new_qty
        print(f'Successfully changed {old_name} quantity to {new_qty}')
        df = pd.DataFrame(self.data)
        print(df) 

    def update_item_price(self):
        old_name = input("Enter the current item name to be modified: ").lower()
        if old_name not in self.data["Item"]:
            print("Item not found")
            return

        new_price = int(input(f"Enter the new qty for {old_name}: "))
        name_index = self.data["Item"].index(old_name) #find the index of old_name
        self.data["Price"][name_index] = new_price
        print(f'Successfully changed {old_name} quantity to {new_price}')
        df = pd.DataFrame(self.data)
        print(df) 

    def delete_item(self):
        item_name = input("Enter which item to remove: ")
        if item_name in self.data["Item"]:
            index = self.data["Item"].index(item_name)
            for key in self.data:
                self.data[key].pop(index)
            print("Item removed successfully.")
        else:
            print("Item not found in the dictionary.")
        df = pd.DataFrame(self.data)
        print(df)

    def reset_transaction(self):
        for key in self.data:     #iterates on dictionary keys
          self.data[key].clear()  #clear values on each keys, this way it only clears the values stored in the list, returning an empty list
        print("Transaction reset successfully.")
        print(self.data)

    def check_order(self):
      null_values = []
      for key, values in self.data.items():
          for i, value in enumerate(values):
              if not value:
                  null_values.append((key, i))

      if null_values:
          print("Null values found in the table:")
          for key, index in null_values:
              print(f"- Key: {key}, Index: {index}")
          print("Please update table!\n Update the table one-by-one, Function will search the null values vertically. Same column first.")
      else:
          print("No null values found in the dictionary.")
      df = pd.DataFrame(self.data)
      print(df)

    def total_price(self):
      total_beforeDisc = sum(self.data["Total Price"])
      total_afterDisc = 0
      if(total_beforeDisc > 500_000):
        disc = 0.1
        total_afterDisc = total_beforeDisc-(total_beforeDisc*disc)
        print(f"Congratulations! You just got 10% discount for spending more than Rp 500.000")
        print(f'Total price: \t{total_beforeDisc}')
        print(f'Discount: \t{disc*100}%')
        print(f'Amount to pay: \t{total_afterDisc}')
      
      elif(total_beforeDisc > 300_000):
        disc = 0.08
        total_afterDisc = total_beforeDisc-(total_beforeDisc*disc)
        print(f"Congratulations! You just got 8% discount for spending more than Rp 300.000")
        print(f'Total price: \t{total_beforeDisc}')
        print(f'Discount: \t{disc*100}%')
        print(f'Amount to pay: \t{total_afterDisc}')

      elif(total_beforeDisc > 200_000):
        disc = 0.05
        total_afterDisc = total_beforeDisc-(total_beforeDisc*disc)
        print(f"Congratulations! You just got 5% discount for spending more than Rp 200.000")
        print(f'Total price: \t{total_beforeDisc}')
        print(f'Discount: \t{disc*100}%')
        print(f'Amount to pay: \t{total_afterDisc}')

      else:
        total_afterDisc=total_beforeDisc
        print(f'Amount to pay: \t{total_afterDisc}')