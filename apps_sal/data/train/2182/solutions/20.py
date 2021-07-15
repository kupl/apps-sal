a = sorted(input())
b = sorted(input(), reverse=True)
n = len(a)
a = ''.join(a[:(n+1)//2])
b = ''.join(b[:n//2])
name = ['']*(len(a)+len(b))

ia = ib = ic = 0
ja = len(a)-1
jb = len(b)-1
jc = len(name)-1
turn = 1
while ic <= jc:
    if turn == 1:
        if ib > jb: name[ic] = a[ia]; ic+= 1
        elif a[ia] < b[ib]: name[ic] = a[ia]; ia+= 1; ic+= 1
        else: name[jc] = a[ja]; ja-= 1; jc-= 1
    else:
        if ia > ja: name[ic] = b[ib]; ic+= 1
        elif b[ib] > a[ia]: name[ic] = b[ib]; ib+= 1; ic+= 1
        else: name[jc] = b[jb]; jb-= 1; jc-= 1
    turn = 3-turn
print(''.join(name))
