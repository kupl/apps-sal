import math

effectiveness = {
    "electric":{
      "electric": 0.5,
      "fire": 1,
      "grass": 1,
      "water": 2
    },
    "fire":{
      "electric": 1,
      "fire": 0.5,
      "grass": 2,
      "water": 0.5
    },
    "grass":{
        "electric": 1,
        "fire": 0.5,
        "grass": 0.5,
        "water": 2
    },
    "water":{
        "electric": 0.5,
        "fire": 2,
        "grass": 0.5,
        "water": 0.5
    }
}

def calculate_damage(your_type, opponent_type, attack, defense):
    return math.ceil(50 * (attack / defense) * effectiveness[your_type][opponent_type]);
