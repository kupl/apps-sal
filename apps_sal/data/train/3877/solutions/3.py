def T9(words, seq):
    ans = []
    for i in words:
        if i.lower().translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', '22233344455566677778889999')) == seq:
            ans += [i]
    return ans if ans else [seq.translate(str.maketrans('23456789', 'adgjmptw'))]
