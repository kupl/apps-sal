while True:
    s = input()
    t = ''.join(set(s))
    if len(s) != len(t) or not s.isalnum():
        print('Invalid')
        continue
    print('Valid')
    break
