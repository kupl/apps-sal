def compress(sentence):
    t = []
    for i in sentence.lower().split(" "):
        if i.lower() not in t:
            t.append(i)
    return "".join([str(t.index(i.lower())) for i in sentence.split(" ")]) if sentence else "" 
