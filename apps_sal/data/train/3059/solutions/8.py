def rain_amount(m): return ["Your plant has had more than enough water for today!", "You need to give your plant {}mm of water"][m < 40].format(40 - m)
