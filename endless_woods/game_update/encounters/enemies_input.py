#File where enemies can be edited and added

def create_enemy_list():
        # Goblins are weaker smaller creatures
    goblin = {"encounter description": "a goblin stands on the side of the road. It looks like he is ready to attack you!",
        "fight": 0.7,
        "run" : 0.5,
        "talk" : 0.3,
        "distract" : 0.3,
        "name" : "goblin"
        }

        # Orcs are bigger stronger creatures
    orc = {"encounter description": "an orc stands on the side of the road. It looks like he is ready to attack you!",
        "fight": 0.3,
        "run" : 0.5,
        "talk" : 0.3,
        "distract" : 0.7,
        "name" : "orc"
        }

            # Orcs are bigger stronger creatures
    wizard = {"encounter description": "an wizard stands on the side of the road. Hard to say if he is evil.",
        "fight": 0.3,
        "run" : 0.5,
        "talk" : 0.7,
        "distract" : 0.3,
        "name" : "wizard"
        }

    enemies_list = [goblin, orc, wizard]

    return enemies_list