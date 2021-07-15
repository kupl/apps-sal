def HQ9(code):
    if code == 'H': return "Hello World!"
    if code == 'Q': return code

    if code == '9':
        lyrics = ''
        for i in range(98):
            current_bottle = 99 - i
            next_bottle = 98 - i
            current_bottle_text = 'bottles' if current_bottle > 1 else 'bottle'
            next_bottle_text = 'bottles' if next_bottle > 1 else 'bottle'
            lyrics += f"{current_bottle} {current_bottle_text} of beer on the wall, {current_bottle} {current_bottle_text} of beer.\nTake one down and pass it around, {next_bottle} {next_bottle_text} of beer on the wall.\n"

        lyrics+= "1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n"
        lyrics+= "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
        return lyrics
    else:
        return None

