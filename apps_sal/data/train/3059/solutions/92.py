def rain_amount(mm):
    if (mm < 40):
        sum=40 - mm
        return "You need to give your plant " + str(sum) + "mm of water"
    else:
         return "Your plant has had more than enough water for today!"
