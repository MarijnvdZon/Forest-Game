def collecting_character_name():
        #Initializing
    allowed_answers_name = ["yes", "no"]
    name_check_done = ("no")

    while name_check_done == "no":
            # Ask player for a character name.
        getting_character_name = input("Enter the name of your adventurer: ")
            # Check with player if they agree on the name.
        name_check_yn = input("So your adventurer is called " + getting_character_name + "? ")
        if name_check_yn.lower() not in allowed_answers_name:
            # Handle invalid input.
            while name_check_yn.lower() not in allowed_answers_name:
                name_check_yn = input("Invalid input. Please enter yes or no: ")

            # End when the player agreed on the name.
        if name_check_yn.lower() == "yes":
            name_check_done = ("yes")

    return getting_character_name