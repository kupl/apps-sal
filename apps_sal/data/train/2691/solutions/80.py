def solve(s):
    l = []
    num = ''
    alp = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    for i in s:
        if i not in alp:
            num += i
        if i in alp:
            if len(num) == 0:
                continue
            else:
                l.append(int(num))
                num = ''
    if len(num) > 0:
        l.append(int(num))
    return max(l)
