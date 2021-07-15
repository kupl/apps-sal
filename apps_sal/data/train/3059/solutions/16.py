def rain_amount(m):
    if m >= 40:
        return "Your plant has had more than enough water for today!"
    else:
          return f"You need to give your plant {40-m}mm of water"
