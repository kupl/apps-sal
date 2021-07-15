import itertools

def merge(l):
    return ''.join(l)

def solve(a,b):
    digits=['3', '5', '8','']
    c2=set(map(merge,itertools.product(digits,digits,digits,digits,digits,digits)))
    c2.remove('')
    c=0
    for n in c2:
        if int(n)>=a and int(n)<b:
               if n.count('8')>= n.count('5') and n.count('5')>= n.count('3'):
                    c+=1
    return c


