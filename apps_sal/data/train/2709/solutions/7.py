chance = {"rainy":-1, "cloudy":0.20, "sunny":0.50}

def take_umbrella(weather, rain_chance):
    return chance[weather] < rain_chance
