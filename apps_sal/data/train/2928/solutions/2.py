def alphabet_war(fight):
    #your code here
    sum = 0
    for i in fight:
      if i == "w":
          sum = sum + 4
      elif i == "p":
           sum = sum + 3
      elif i == "b":
           sum = sum + 2
      elif i == "s":
           sum = sum + 1
      elif i == "m":
           sum = sum - 4
      elif i == "q":
           sum = sum - 3
      elif i == "d":
           sum = sum - 2
      elif i == "z":
           sum = sum - 1
      
             
    if sum > 0:
        return  "Left side wins!"
    elif sum == 0:
        return "Let's fight again!"
    else:
        return "Right side wins!"
