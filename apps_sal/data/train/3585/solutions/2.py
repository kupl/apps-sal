def proc_seq(*li):
    un = {(i,) for i in str(li[0]) if i[0] != '0'}
    for i in li[1:]:
        un = {k + (l,) for k in un for l in str(i)}
    un = {int(''.join(i)) for i in un}
    return [1, un.pop()] if len(un) == 1 else [len(un), min(un), max(un), sum(un)]
