from game_functions.get_name import collecting_character_name
from game_update.stats_input import make_stats
from game_functions.visual.stats_show import show_stats
from game_functions.get_path_choice import get_path
from game_functions.get_encounter import get_encounter_description
from game_functions.visual.line_show import line_art
from game_update.path_input import path_descriptions_list
from game_update.encounters.enemies_input import create_enemy_list
from game_functions.get_result import encounter_result
from game_functions.continue_game import collecting_game_state


    # Load in all enemies of the game
enemies_list = create_enemy_list()

    # Set game to playable
game_state = "yes"

    # Introduction text to the game
print(line_art)
print("Welcome to the Endless Woods! You are an adventurer who will try to survive in these woods.")

    # Get name from player
print(line_art)    
character_name = collecting_character_name()

    # Create character stats
character_list = make_stats(character_name)

while game_state == "yes":
        # Getting the player to pick a path, returns path #number
    print(line_art)
    path_choice = get_path()

        # Choosing and describing the encounter
    print(line_art)
    encounter_choice = get_encounter_description(path_choice, enemies_list, character_name)

        # generate result of the encounter
    print(line_art)
    character_list = encounter_result(enemies_list, encounter_choice, character_list)

    print(line_art)
    show_stats(character_list)

        # check if the players wants to keep on playing
    print(line_art)
    game_state = collecting_game_state()