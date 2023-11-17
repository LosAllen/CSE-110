def start_game():
    print("Welcome to the Magical Forest Adventure!")
    print("You find yourself at a crossroads in the forest. Two paths lie ahead.")
    print("1. TAKE THE LEFT PATH")
    print("2. TAKE THE RIGHT PATH")

    user_choice = str(input("What will you do? "))

    if user_choice.upper() == "TAKE THE LEFT PATH":
        print("You venture down the left path and come across a mystical creature.")
        print("The creature seems to be friendly. How will you approach it?")
        print("1. OFFER A GIFT")
        print("2. ASK FOR INFORMATION")
        print("3. IGNORE AND WALK AWAY")

        user_choice = str(input("Your choice: "))

        if user_choice.upper() == "OFFER A GIFT":
            print("The creature appreciates your gift and grants you a magical token.")
            print("As you continue your journey, you encounter a magical bridge.")
            print("1. CROSS THE BRIDGE")
            print("2. TURN BACK")

            user_choice = str(input("Your choice: "))

            if user_choice.upper() == "CROSS THE BRIDGE":
                print("The bridge leads you to a hidden grove where you discover a treasure chest.")
                print("Congratulations! You've found a stash of magical artifacts.")
            elif user_choice.upper() == "TURN BACK":
                print("You decide not to cross the bridge and continue exploring the mystical forest.") 
            else:
                print("Sorry, that's not a valid choice. Please restart the game and choose a valid option.")

        elif user_choice.upper() == "ASK FOR INFORMATION":
            print("The creature shares valuable information about the forest's secrets.")
            print("With the newfound knowledge, you come across a magical pool.")
            print("1. DRINK FROM THE POOL")
            print("2. BYPASS THE POOL")

            user_choice = str(input("Your choice: "))

            if user_choice.upper() == "DRINK FROM THE POOL":
                print("Drinking from the pool enhances your magical abilities.")
                print("You now feel more attuned to the mystical energy of the forest.")
            elif user_choice.upper() == "BYPASS THE POOL":
                print("You decide not to drink from the pool and continue your journey.")
            else:
                print("Sorry, that's not a valid choice. Please restart the game and choose a valid option.")

        elif user_choice.upper() == "IGNORE AND WALK AWAY":
            print("You decide to ignore the creature and continue your journey.")
            print("Further down the path, you encounter a magical tree.")
            print("1. CLIMB THE TREE")
            print("2. WALK AROUND THE TREE")

            user_choice = str(input("Your choice: "))

            if user_choice.upper() == "CLIMB THE TREE":
                print("Climbing the tree grants you a panoramic view of the entire forest.")
                print("You spot a hidden path that leads to a magical garden.")
                print("Congratulations! You've discovered a serene and enchanting garden.")
            elif user_choice.upper() == "WALK AROUND THE TREE":
                print("Walking around the tree, you find a hidden path leading to a mystical spring.")
                print("The spring has healing properties. You feel rejuvenated.")
            else:
                print("Sorry, that's not a valid choice. Please restart the game and choose a valid option.")
        else:
            print("Sorry, that's not a valid choice. Please restart the game and choose a valid option.")
    
    elif user_choice.upper() == "TAKE THE RIGHT PATH":
        print("You follow the right path and encounter a mysterious door.")
        print("The door seems to be enchanted. What will you do?")
        print("1. KNOCK ON THE DOOR")
        print("2. TRY TO OPEN THE DOOR")
        print("3. LEAVE THE DOOR AND CONTINUE")

        user_choice = str(input("Your choice: "))

        if user_choice.upper() == "KNOCK ON THE DOOR":
            print("A magical being opens the door and offers to grant you a wish.")
            print("1. MAKE A WISH")
            print("2. DECLINE AND CONTINUE")

            user_choice = str(input("Your choice: "))

            if user_choice.upper() == "MAKE A WISH":
                print("Your wish is granted, and you feel a surge of magical energy.")
                print("With your newfound power, you come across a hidden cave.")
                print("1. ENTER THE CAVE")
                print("2. CONTINUE PAST THE CAVE")

                user_choice = str(input("Your choice: "))

                if user_choice.upper() == "ENTER THE CAVE":
                    print("Inside the cave, you find a legendary artifact.")
                    print("Congratulations! You've discovered a powerful magical relic.")
                elif user_choice.upper() == "CONTINUE PAST THE CAVE":
                    print("You decide not to enter the cave and continue exploring the enchanted forest.")
                else:
                    print("Sorry, that's not a valid choice. Please restart the game and choose a valid option.")

            elif user_choice.upper() == "DECLINE AND CONTINUE":
                print("You decline the offer and continue your journey.")
                
            else:
                print("Sorry, that's not a valid choice. Please restart the game and choose a valid option.")

        elif user_choice.upper() == "TRY TO OPEN THE DOOR":
            print("The door resists your attempt, and you sense a magical barrier.")
            print("You decide to leave it for now and continue down the path.")
            print("As you walk, you encounter a mystical fountain.")
            print("1. MAKE A WISH AT THE FOUNTAIN")
            print("2. IGNORE AND CONTINUE")

            user_choice = str(input("Your choice: "))

            if user_choice.upper() == "MAKE A WISH AT THE FOUNTAIN":
                print("Your wish at the fountain comes true, and you feel a renewed sense of purpose.")
                print("You discover a hidden trail that leads to a magical meadow.")
                print("Congratulations! You've found a peaceful and magical meadow.")
            elif user_choice.upper() == "IGNORE AND CONTINUE":
                print("You decide not to make a wish at the fountain and continue your journey.")
            else:
                print("Sorry, that's not a valid choice. Please restart the game and choose a valid option.")

        elif user_choice.upper() == "LEAVE THE DOOR AND CONTINUE":
            print("You decide not to risk dealing with the mysterious door and continue your journey.")
            print("Further along the path, you encounter a wise old wizard.")
            print("1. ASK FOR ADVICE")
            print("2. IGNORE AND CONTINUE")

            user_choice = str(input("Your choice: "))

            if user_choice.upper() == "ASK FOR ADVICE":
                print("The wizard imparts valuable wisdom about navigating the magical forest.")
                print("With the wizard's advice, you navigate the forest with newfound confidence.")
            elif user_choice.upper() == "IGNORE AND CONTINUE":
                print("You decide not to ask for advice and continue your journey.")
            else:
                print("Sorry, that's not a valid choice. Please restart the game and choose a valid option.")
        else:
            print("Sorry, that's not a valid choice. Please restart the game and choose a valid option.")
                
    elif user_choice.upper() == "I DO NOT WANT TO PLAY":
        print("That is okay. Please elaborate (Why do you not want to play?):")

        user_choice = str(input("Your elaboration: "))

        if user_choice != "qwop":
            print("Thank you for your feedback! We will do better in the future.")
        else:
            print("You just wanted to see this message huh? Well cool, here it is.")
                

    else:
        print("Sorry, that's not a valid choice. Please restart the game and choose a valid option.")

# Start the game
start_game()
