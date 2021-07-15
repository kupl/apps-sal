import re
import string
dic1 = {224:97, 244:111, 252:117, 233:101, 239:105}
def could_be(original, another):
    if original == '' and another == '':
        return False
    p = "!,;:?"
    o, a = original.lower(), another.lower()
    o, a = re.sub(r"[!,;:\?\.]", ' ', o), re.sub(r"[!,;:\?\.]", ' ', a)
    if o == a: return True
    o = o.encode('unicode-escape').decode('unicode-escape')
    a = a.encode('unicode-escape').decode('unicode-escape')
    o1, a1 = o.split(), a.split()
    o2 = [i[:-1] if i[-1] in p else i for i in o1]
    ans1 = []
    for i in o2:
        t = ''
        for j in i:
            t = t + chr(dic1[ord(j)]) if ord(j) in dic1 else t + j
        ans1.append(t)
    
    a2 = [i[:-1] if i[-1] in p else i for i in a1]
    ans2 = []
    for i in a2:
        t = ''
        for j in i:
            t = t + chr(dic1[ord(j)]) if ord(j) in dic1 else t + j
        ans2.append(t)
    if ans1 != [] and ans2 == []:
        return False
    for i in ans2:
        for j in ans1:
            if i == j:
                break
        else:
            return False
    return True
