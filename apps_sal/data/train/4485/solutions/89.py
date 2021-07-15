def HQ9(code):
    if code == "H":
        return "Hello World!"
    elif code == "Q":
        return "Q"
    elif code == "9":
        i = 99
        song = ""
        while i > 2:
            song += f"""{i} bottles of beer on the wall, {i} bottles of beer.
Take one down and pass it around, {i-1} bottles of beer on the wall.
"""
            i -= 1
        song += """2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall."""
        return song
