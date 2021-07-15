def bottle():
    song = ""
    for i in range(99, 0, -1):
        if(i == 2):
            song += "{} bottles of beer on the wall, {} bottles of beer.\nTake one down and pass it around, {} bottle of beer on the wall.\n".format(i, i, i-1)
        elif(i == 1):
            song += "{} bottle of beer on the wall, {} bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.".format(i, i)
        else:
            song += "{} bottles of beer on the wall, {} bottles of beer.\nTake one down and pass it around, {} bottles of beer on the wall.\n".format(i, i, i-1)
    return song

def HQ9(code):
    return {
        "H" : "Hello World!",
        "Q" : "Q",
        "9" : bottle()
    }.get(code, None)

