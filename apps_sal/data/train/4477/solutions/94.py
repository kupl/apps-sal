def reverse_number(n):
    result=int("".join(reversed(list(str(abs(n))))))
    if n>0:
        return result
    else:
        return -result
