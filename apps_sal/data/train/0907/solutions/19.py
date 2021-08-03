for _ in range(int(input())):
    n = int(input())
    s = input()
    s = s.replace(".", "")
    if len(s) == 0:
        print("Valid")
        continue
    elif len(s) == 1 or s[len(s) - 1] == 'H':
        print("Invalid")
        continue
    for i in range(len(s)):
        if s[i] == "T" and i == 0:
            print("Invalid")
            break
        elif s[i] == 'H':
            if s[i - 1] == 'H':
                print("Invalid")
                break
        elif s[i] == 'T':
            if s[i - 1] == 'T':
                print("Invalid")
                break
    else:
        print("Valid")
