import string
def position(alphabet):
    d={}
    s=string.ascii_lowercase
    c=1
    for i in s:
        d[i]=c
        c+=1
    return f'Position of alphabet: {d.get(alphabet)}'
