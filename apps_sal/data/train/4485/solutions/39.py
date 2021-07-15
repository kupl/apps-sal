def HQ9(code):
    
    full_song = []
    beer = 99
    for i in range(2, beer):
        lyric = f"""{beer} bottles of beer on the wall, {beer} bottles of beer.""" + '\n' + \
            f"""Take one down and pass it around, {beer - 1} bottles of beer on the wall."""
    
        beer -= 1
        full_song.append(lyric)
    
    
    end = "2 bottles of beer on the wall, 2 bottles of beer." + "\n" + "Take one down and pass it around, 1 bottle of beer on the wall." + "\n" + "1 bottle of beer on the wall, 1 bottle of beer." + "\n" + \
        "Take one down and pass it around, no more bottles of beer on the wall." + "\n" + \
        "No more bottles of beer on the wall, no more bottles of beer." + "\n" + \
        "Go to the store and buy some more, 99 bottles of beer on the wall."
    full_song.append(end)
    
    output_song = '\n'.join(full_song)
    
    phrase = {
        'H':'Hello World!',
        'Q': 'Q',
        '9': output_song
    }
    
    return phrase.get(code, None)
