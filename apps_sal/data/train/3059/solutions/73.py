def rain_amount(mm):
    if (mm >= 40):
         return "Your plant has had more than enough water for today!"
    elif (mm < 40):
         return ("You need to give your plant {}mm of water".format(40 - mm))
