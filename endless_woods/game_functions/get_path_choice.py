import random
from game_update.path_input import path_descriptions_list

def get_path():
    allowed_answers_path = [1, 2]
        # Randomization math can be done here!!!  ############################################################# <--- Math spot!!
    random_number1 = random.randint(1,10)
    random_number2 = random.randint(1,10)
        # Make sure the numbers are not the same
    while random_number1 == random_number2:
        random_number2 = random.randint(1,10)

        # Print text for player and ask for a choice of path
    print("In the woods you stumble upon a intersection on the road. There are 2 paths leading foreward.")
    print("(1)", path_descriptions_list[random_number1])
    print("(2)", path_descriptions_list[random_number2])

        # Get response from player what path they want
    while True:
        try:
            path_choice = int(input("[QUESTION] What path do you take?: "))

            if path_choice not in allowed_answers_path:
                print("[Invalid input] Please enter 1 or 2: ")
            else:
                break
        except ValueError:
            print("[Invalid input] Please enter 1 or 2: ")

        # Return the number of the chosen path
    if path_choice == 1:
        return random_number1

    return random_number2