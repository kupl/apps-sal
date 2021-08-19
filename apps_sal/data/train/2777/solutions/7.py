def solve(a):
    (sta, exp) = ('', '')
    for i in a[::-1]:
        if i.isalnum() or i == '(':
            if i == '(':
                exp += sta
                sta = ''
            elif ord(i) in range(48, 58):
                exp = exp * int(i)
            else:
                sta += i
    return exp[::-1] if a[0].isnumeric() else a[0] + exp[::-1]
