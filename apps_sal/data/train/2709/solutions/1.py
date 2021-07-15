def take_umbrella(weather, rain_chance):
    return rain_chance > {'sunny': 0.5, 'cloudy': 0.2, 'rainy': -1}[weather]
