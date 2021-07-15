def HQ9(code):
    if code == "H":
        return "Hello World!"
    if code == "Q":
        return code
    if code == "9":
        return_string = ""
        for x in range(99, 1, -1):
            if x != 99:
                return_string = return_string + "Take one down and pass it around, " + str(x) + " bottles of beer on the wall.\n"
            return_string = return_string + str(x) + ' bottles of beer on the wall, ' + str(x) + ' bottles of beer.\n'
        return_string = return_string + "Take one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
        return return_string    
    pass
