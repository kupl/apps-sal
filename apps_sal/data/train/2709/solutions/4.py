def take_umbrella(weather, rain_chance):
    return weather == 'rainy' or rain_chance > 0.5 or (weather == 'cloudy' and rain_chance > 0.2)
