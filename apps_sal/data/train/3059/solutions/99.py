def rain_amount(m):
   if m <40:
     return "You need to give your plant {}mm of water".format(abs(m - 40))
   else:
     return "Your plant has had more than enough water for today!"
