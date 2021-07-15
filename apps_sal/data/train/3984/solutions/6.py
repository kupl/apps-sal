dict = {'a':'beef', 
        'e':'beef',
        'i':'beef', 
        'o':'beef', 
        'u':'beef', 
        't':'tomato', 
        'l':'lettuce', 
        'c':'cheese', 
        'g':'guacamole', 
        's':'salsa'}
        
def tacofy(word):
    # Start with the shell
    outlist = ['shell']
    # Don't forget we're case insensitive!
    for c in word.lower():
        # Is this letter one of the taco ones?  Find its ingredient!
        if c in dict: # Python 3.0 doesn't have dictionary.has_key()
            outlist.append(dict.get(c))
    # Don't forget the final shell wrapper!
    outlist.append('shell')
    return outlist
