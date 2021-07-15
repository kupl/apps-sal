def rain_amount(mm):

    rain_amount = 40
    
    if mm < rain_amount:
         return f"You need to give your plant {rain_amount - mm }mm of water"
    else:
         return "Your plant has had more than enough water for today!"
