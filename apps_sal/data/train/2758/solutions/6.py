def decode(number):
    parts = [e for e in str(number).split('98') if e]
    return ', '.join(str(int(w, 2)) if i % 2 else word(w) for i, w in enumerate(parts))
        
def word(s):
    return ''.join(chr(int(s[i*3:i*3+3]) - 4) for i in range(len(s) // 3))        
