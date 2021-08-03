def take_umbrella(weather, rain_chance):
    # Your code here.
    return (weather == 'cloudy' and rain_chance > 0.20) or weather == 'rainy' or (weather == 'sunny' and rain_chance > 0.5)
