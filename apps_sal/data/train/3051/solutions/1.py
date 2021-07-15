def to_nato(words):
    l = """Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar 
           Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey Xray Yankee Zulu"""
    d = {w[0]:w for w in l.split()}
    return ' '.join(d.get(c, c) for c in words.upper() if c != ' ')

