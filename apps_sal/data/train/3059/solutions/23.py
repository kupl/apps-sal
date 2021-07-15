def rain_amount(mm):
    rain = 40 - mm
    rain = str(rain)
    if mm < 40:
          return("You need to give your plant " + rain + "mm of water")
    
    else:
        return( "Your plant has had more than enough water for today!")
