for _ in range(int(input())):
    has = input()
    while 'abc' in has:
        has = has.replace('abc', '')
    print(has)
