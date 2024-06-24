# Basic script to add cards/fields for the game using dataloader, json file

from dataLoader import DataLoader

file_Path = "data.json"
dl = DataLoader(file_Path)
dl.read_Json()

while True:
    print()
    print("Enter 1 to view current fields")
    print("Enter 2 to view current monster cards")
    print("Enter 3 to view current spell cards")
    print("Enter 4 to create a new field/card")
    menuSelect = input("Enter 0 to exit\n")
    print()

    if menuSelect == "0":
        break

    elif menuSelect == "1":
        dl.display_Json(["fields"])

    elif menuSelect == "2":
        dl.display_Json(["cards", "monsters"])

    elif menuSelect == "3":
        dl.display_Json(["cards", "spells"])

    elif menuSelect == "4":
        print("Enter 1 to create a new field")
        print("Enter 2 to create a new spell")
        print("Enter 3 to create a new monster")
        cardMenuSelect = input("Enter 0 to return to the previous menu\n")
        print()

        if cardMenuSelect not in ["1", "2", "3"]:
            continue

        new_Object = {}

        new_Object["name"] = input("Enter a name: ").title()
        new_Object["element"] = input("Enter an element: ").capitalize()
        new_Object["effect"] = input("Enter an effect: ")

        if cardMenuSelect == "1":
            dl.append_Json(new_Object, ["fields"])
        else:
            new_Object["resource_Cost"] = int(input("Enter the resource cost: "))
            new_Object["resource_Type"] = input("Enter the resource type (blood/mana): ").capitalize()

            if cardMenuSelect == "2":
                new_Object["spell_Type"] = input("Enter a spell type (equipment, legend, etc.): ").capitalize()
                dl.append_Json(new_Object, ["cards", "spells"])

            elif cardMenuSelect == "3":
                new_Object["species"] = input("Enter the species: ").capitalize()
                new_Object["attack"] = int(input("Enter the attack value: "))
                new_Object["defense"] = int(input("Enter the defense value: "))
                dl.append_Json(new_Object, ["cards", "monsters"])
        
        dl.save_Json()
