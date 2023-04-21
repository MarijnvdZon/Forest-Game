import random

def encounter_result(enemies_list, encounter_choice, character_list):

    random_number = random.random()

    if encounter_choice[0] == 1:
        if random_number <= enemies_list[encounter_choice[1]]["fight"]:
            print("You attack the", enemies_list[encounter_choice[1]]["name"], "and the", enemies_list[encounter_choice[1]]["name"], "get killed!")
            character_list["Fights won:"] += 1
        else:
            print("You attack the", enemies_list[encounter_choice[1]]["name"], "and you fail, the", enemies_list[encounter_choice[1]]["name"], "hits you before you get past him!")
            character_list["Hp:"] -= 1

    elif encounter_choice[0] == 2:
        if random_number <= enemies_list[encounter_choice[1]]["run"]:
            print("You run past the", enemies_list[encounter_choice[1]]["name"], "and leave the", enemies_list[encounter_choice[1]]["name"], "behind!")
            character_list["Fights won:"] += 1
        else:
            print("You try to run past the", enemies_list[encounter_choice[1]]["name"], "but you get hit by the", enemies_list[encounter_choice[1]]["name"], "before you get past him!")
            character_list["Hp:"] -= 1

    elif encounter_choice[0] == 3:
        if random_number <= enemies_list[encounter_choice[1]]["talk"]:
            print("You talk to the", enemies_list[encounter_choice[1]]["name"], "man. The", enemies_list[encounter_choice[1]]["name"], "is nice and lets you past!")
            character_list["Fights won:"] += 1
        else:
            print("You talk to the", enemies_list[encounter_choice[1]]["name"], "man. But the", enemies_list[encounter_choice[1]]["name"], "didn't want to talk and hits you before you get away!")
            character_list["Hp:"] -= 1

    else:
        if random_number <= enemies_list[encounter_choice[1]]["distract"]:
            print("You distract the", enemies_list[encounter_choice[1]]["name"], "with a rock. It works and you leave the", enemies_list[encounter_choice[1]]["name"], "behind")
            character_list["Fights won:"] += 1
        else:
            print("You distract the", enemies_list[encounter_choice[1]]["name"], "with a rock. The", enemies_list[encounter_choice[1]]["name"], "uses the rock to hit you before you get past him!")
            character_list["Hp:"] -= 1

    return character_list