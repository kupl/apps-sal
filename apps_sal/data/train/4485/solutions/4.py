def HQ9(code):
    if code == "H":
        return "Hello World!"
    if code == "Q":
        return "Q"
    if code == "9":
        result = ""
        for n in range(99, 2, -1):
            result += f"{n} bottles of beer on the wall, {n} bottles of beer.\nTake one down and pass it around, {n-1} bottles of beer on the wall.\n"
        result += "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
        return result
    return None
