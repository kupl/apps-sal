def rain_amount(mm):
    return "Your plant has had more than enough water for today!" if mm>40 else "Your plant has had more than enough water for today!" if mm==40 else "You need to give your plant {}mm of water".format(str(40-mm))
