def sorted_brands(history):
    s = [i['brand'] for i in history]
    print(s)
        
    return sorted(set(s), key=lambda x: (-s.count(x), s.index(x)))
