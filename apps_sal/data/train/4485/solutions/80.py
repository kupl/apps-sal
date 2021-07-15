BEER = "bottles of beer"

def HQ9(code):
    if code == "H":
        return "Hello World!"
    elif code == "Q":
        return code
    elif code == "9":
        lyrics = "\n".join(
        ["{0} {1} on the wall, {0} {1}.\nTake one down and pass it around, {2} {1} on the wall."
         .format(i, BEER, i-1) for i in range(99, 2, -1)]
        )
        lyrics += "\n2 bottles of beer on the wall, 2 bottles of beer.\n" + \
            "Take one down and pass it around, 1 bottle of beer on the wall.\n" + \
            "1 bottle of beer on the wall, 1 bottle of beer.\n" + \
            "Take one down and pass it around, no more bottles of beer on the wall.\n" + \
            "No more bottles of beer on the wall, no more bottles of beer.\n" + \
            "Go to the store and buy some more, 99 bottles of beer on the wall."
        return lyrics
