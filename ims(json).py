#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import json

class Inventory:
    def _init_(self):
        #AT LAUNCH GROUPS AND LOADING FUNCTION
        self.items = {}
        self.load()

    def remove(self, ID):
        #REMOVING ITEMS FOR LISTS AND OUTPUT DOCUMENT
        del self.items[str(ID)]
        self.save()

    def add(self, ID, name, qty):
        #ADDING ITEMS FOR LISTS AND OUTPUT DOCUMENT
        self.items[ID] = {"name": name, "qty": qty}
        self.save()

    def update(self, ID, update):
        #UPDATING ITEMS FOR LISTS AND OUTPUT DOCUMENT
        self.items[ID]["qty"] += update
        self.save()

    def search(self, ID):
        #SEARCHING ITEMS FOR LISTS
        item = self.items.get(ID, None)
        if item:
            return ID, item['name'], item['qty']
        else:
            return None

    def _str_(self):
        #FORMATTING
        out = ""
        for id, d in self.items.items():
            out += f"ID Number : {id} \nItem Name : {d['name']}\nQuantity : {d['qty']}\n"
            out += "----------\n"
        return out
    
    def save(self):
        #WHERE TO SAVE TO
        with open('data.txt','w') as outfile:
           json.dump(self.items, outfile)

    def load(self):
        #WHERE TO PUT DATA FROM WHEN RELAUNCHING PROGRAM
        try:
            with open('data.txt','r') as json_file:
               self.items = json.load(json_file)
        except:
            print("Can't load old inventory, starting fresh")
            self.items = {}


def menuDisplay():
    #MENU FOR PROGRAM 
    """Display the menu"""
    print('=============================')
    print('= Inventory Management Menu =')
    print('=============================')
    print('(1) Add New Item to Inventory')
    print('(2) Remove Item from Inventory')
    print('(3) Update Inventory')
    print('(4) Search Item in Inventory')
    print('(5) Print Inventory Report')
    print('(99) Quit')


def add_one_item(inventory):
    #ADDING PROMPT AND ERROR CHECKING
    print('Adding Inventory')
    print('================')
    while True:
        try:
            new_ID = int(input("Enter an ID number for the item: "))
            if inventory.search(new_ID):
                print("ID number is taken, please enter a different ID number")
                continue
            new_name = input('Enter the name of the item: ').lower()
            assert new_name.isalpha(), "Only letters are allowed!"
            new_qty = int(input("Enter the quantity of the item: "))
            inventory.add(new_ID, new_name, new_qty)
            break
        except Exception as e:
            print("Invalid choice! try again! " + str(e))
            print()


def remove_one_item(inventory):
    #REMOVING PROMPT AND ERROR CHECKING
    print('Removing Inventory')
    print('==================')
    removing = int(input("Enter the item's ID number to remove from inventory: "))
    inventory.remove(removing)


def ask_exit_or_continue():
    #OPTION TO CONTINUE OR QUITE PROGRAM
    return int(input('Enter 98 to continue or 99 to exit: '))


def update_inventory(inventory):
    #UPDATING PROMPT AND ERROR CHECKING
    print('Updating Inventory')
    print('==================')
    ID = int(input("Enter the item's ID number to update: "))
    update = int(input("Enter the updated quantity. Enter 5 for additional or -5 for less: "))
    inventory.update(ID, update)


def search_inventory(inventory):
    #SEARCHING PROMPT AND ERROR CHECKING
    print('Searching Inventory')
    print('===================')
    search = int(input("Enter the ID number of the item: "))
    result = inventory.search(search)
    if result is None:
        print("Item not in inventory")
    else:
        ID, name, qty = result
        print('ID Number: ', ID)
        print('Item:     ', name)
        print('Quantity: ', qty)
        print('----------')


def print_inventory(inventory):
    #PRINT CURRENT LIST OF ITEMS IN INVENTORY
    print('Current Inventory')
    print('=================')
    print(inventory)


def main():
    #PROGRAM RUNNING COMMAND AND ERROR CHECKING
    inventory = Inventory()
    while True:
        try:
            menuDisplay()
            CHOICE = int(input("Enter choice: "))
            if CHOICE in [1, 2, 3, 4, 5]:
                if CHOICE == 1:
                    add_one_item(inventory)
                elif CHOICE == 2:
                    remove_one_item(inventory)
                elif CHOICE == 3:
                    update_inventory(inventory)
                elif CHOICE == 4:
                    search_inventory(inventory)
                elif CHOICE == 5:
                    print_inventory(inventory)
                exit_choice = ask_exit_or_continue()
                if exit_choice == 99:
                    exit()
            elif CHOICE == 99:
                exit()
        except Exception as e:
            print("Invalid choice! try again!"+str(e))
            print()

        # If the user pick an invalid choice,
        # the program will come to here and
        # then loop back.


main()

