    #[f(x) if condition else g(x) for x in sequence]
    #[f(x) for x in sequence if condition]
def reverse_number(n):
    if str(n)[0]=="-":
        new = int("-"+''.join([str(n)[1:][-1-i] for i in range(len(str(n))-1) ]))
    else:
        new = int(''.join([str(n)[-1-i] for i in range(len(str(n))) ]))

    if new ==0:
        return new
    else:
        return int(str(new).lstrip("0"))

