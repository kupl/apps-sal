import re
def encoder(s):
    d, numbers, i, li = {}, iter(range(1, 1000)), 0, []
    while i < len(s):
        symbol = s[i]
        prev = 0
        while symbol in d:
            i += 1 ; prev = d[symbol]
            if i == len(s) : return "".join(li)+str(d[symbol])
            symbol += s[i]
        d[symbol] = next(numbers)
        li.append(str(prev) + s[i])
        i += 1
    return "".join(li)
    
def decoder(s):
    parts, numbers, d, li = re.findall(r'\d+[A-Z]', s), iter(range(1, 1000)), {}, []
    for i in parts:
        if re.fullmatch(r'\d+\w', i):
            t = re.findall(r'(\d+)(\w)',i)
            k, l = int(t[0][0]), t[0][1]
            if not k : d[next(numbers)] = l ; li.append(l)
            else : d[next(numbers)] = d[k] + l ; li.append(d[k] + l)
        else : li.append(d[int(i)])
    p = len(s)-len(''.join(parts))
    return ''.join(li) + (d[int(s[-p:])] if s[-p:].isdigit() else '')
