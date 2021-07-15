import re
def encode(st):
    vowel = ' aeiou'
    return re.sub(r'[aeoui]', lambda x: str(vowel.index(x.group(0))) ,st)
    
def decode(st):
    vowel = ' aeiou'
    return re.sub(r'[1-5]', lambda x: vowel[int(x.group(0))] ,st)

