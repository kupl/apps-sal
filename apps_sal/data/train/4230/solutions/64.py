def reverse_letter(a):
    ans = ''
    a = list(a)
    while len(a) > 0:
        b = a.pop()
        if b.isalpha():
            ans = ans + b
            print(ans)
    return ans
