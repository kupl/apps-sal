def take_umbrella(weather, rain_chance):
  return { weather == "rainy": True, weather == "cloudy" and rain_chance > 0.2: True,
           weather == "sunny" and rain_chance > 0.5: True}.get(True, False)
