arr = {'sunny': 0.50, 'rainy': -1.0, 'cloudy': 0.20}


def take_umbrella(weather, rain_chance):
    return rain_chance > arr[weather]
