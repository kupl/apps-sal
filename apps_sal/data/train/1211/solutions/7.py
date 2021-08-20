t = int(input())
for i in range(t):
    str_ = input()
    while True:
        if 'abc' in str_:
            str_ = str_.replace('abc', '')
        else:
            break
    print(str_)
