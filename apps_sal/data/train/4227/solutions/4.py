import re
def complexSum(arr):
    real=0
    img=0
    for a in arr:
        for b in re.findall(r'[-+]?\d*i?',a):
            if not b:
                continue
            if 'i' in b:
                if b=='+i' or b=='i':
                    img+=1
                elif b=='-i':
                    img-=1
                else:
                    img+=int(b[:-1])
            else:
                real+=int(b)

    if img==0:
        return str(real)
    elif real==0:
        if img==1:
            return 'i'
        elif img==-1:
            return '-i'
        else:
            return '{}i'.format(img)
    else:
        return '{}{:+}i'.format(real,img).replace('+1i','+i').replace('-1i','-i')
