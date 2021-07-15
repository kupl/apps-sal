rain_amount = lambda mm: ('Your plant has had more than enough water for today!','You need to give your plant %dmm of water'%(40-mm))[mm<40]
