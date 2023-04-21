import random

from game_update.path_input import path_descriptions_list
from game_update.encounters.enemies_input import create_enemy_list
    # Generate a encounter based on chosen path

def get_encounter_description(path, enemies_list, character_name):

    allowed_answers_encounter = [1, 2, 3, 4]
    
        # Choose a random enemy from the list
    random_enemy_number = random.randint(1,len(enemies_list)) - 1

        # Show options to the player
    print(character_name, "takes a long walk on", path_descriptions_list[path])
    print(enemies_list[random_enemy_number]["encounter description"])
    print(character_name, "sees four options to get further along the road.")
    print("(1) Fight")
    print("(2) Run")
    print("(3) Talk")
    print("(4) Distract")

    # Get response from player what path they want
    while True:
        try:
            encounter_choice = int(input("[QUESTION] What option do you take?: "))

            if encounter_choice not in allowed_answers_encounter:
                print("[Invalid input] Please enter 1, 2, 3 or 4: ")
            else:
                break
        except ValueError:
            print("[Invalid input] Please enter 1, 2, 3 or 4: ")

    return [encounter_choice, random_enemy_number]