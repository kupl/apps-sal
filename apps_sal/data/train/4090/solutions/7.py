def get_animals_count(l, he, ho):
    return {"rabbits": l // 2 - he - ho // 2, "chickens": 2 * he - l // 2, "cows": ho // 2}
