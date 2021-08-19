arr = {'sunny': 0.5, 'rainy': -1.0, 'cloudy': 0.2}


def take_umbrella(weather, rain_chance):
    return rain_chance > arr[weather]
