from string import punctuation

def top_3_words(text):
    for p in punctuation: 
        if p != "'": text = text.replace(p, " ")
    count = {}
    for w in text.lower().split():
        if w.strip(punctuation) == '':
            pass
        elif w in count.keys():
            count[w] += 1
        else:
            count[w] = 1
    lcount = [(w,c) for w,c in count.items()]
    lcount.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in lcount[:3]]
