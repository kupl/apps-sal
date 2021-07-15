def meeting(rooms):
    tally = 0
    for i in rooms:
        if i == "O":
            return tally
        else:
            tally += 1
    return("None available!")
              
             

