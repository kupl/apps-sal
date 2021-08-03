def take_umbrella(weather, rain_chance):
    return (weather == 'rainy') or (weather == 'cloudy' and rain_chance > 0.20)\
        or (rain_chance > 0.50)
