def take_umbrella(weather, rain_chance):
    return (weather == 'cloudy' and rain_chance > .2) or (weather == 'rainy') or (weather == 'sunny' and rain_chance > .5)
