def extract_number(word):
    for l in word: 
        if l.isdigit(): return int(l)
    return None

def order(sentence):
    return ' '.join(sorted(sentence.split(), key=extract_number))

