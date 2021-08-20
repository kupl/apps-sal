chance = {'rainy': -1, 'cloudy': 0.2, 'sunny': 0.5}


def take_umbrella(weather, rain_chance):
    return chance[weather] < rain_chance
