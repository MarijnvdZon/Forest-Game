def collecting_game_state():
        #Initializing
    allowed_answers_name = ["yes", "no"]

    game_state = input("Do you want to keep on playing?: ")
    if game_state.lower() not in allowed_answers_name:
        # Handle invalid input.
        while game_state.lower() not in allowed_answers_name:
            game_state = input("Invalid input. Please enter yes or no: ")

    return game_state