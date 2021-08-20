def take_umbrella(weather, rain_chance):
    return weather == 'rainy' or (weather == 'cloudy' and rain_chance > 0.2) or rain_chance > 0.5
