from itertools import chain

def change(st):
    if len(st) < 4: return st
    q, r = divmod(len(st), 2)
    return ''.join(chain(st[q-1::-1], st[q:q+r], st[:q+r-1:-1]))

def inside_out(st):
    return ' '.join(map(change, st.split()))
