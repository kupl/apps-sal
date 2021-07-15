def HQ9(code):
    if code == "H":
        return "Hello World!"
    if code == "Q": return "Q"
    
    if code == "9":
        res =""
        for i in range(2,99):
            res += f"{101-i} bottles of beer on the wall, {101-i} bottles of beer.\nTake one down and pass it around, {100-i} bottles of beer on the wall.\n"
        res += "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n"
        res +="1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
        
        return res
    return None

