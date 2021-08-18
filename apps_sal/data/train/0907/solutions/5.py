for z in range(int(input())):
    n = int(input())
    s = input()
    s = s.replace('.', '')
    l = len(s)
    if l % 2 != 0:
        print("Invalid")
    elif l == 0:
        print("Valid")
    elif s[0] != 'H' or s[-1] != 'T':
        print("Invalid")
    else:
        for i in range(l - 1):
            if s[i] == s[i + 1]:
                print("Invalid")
                break
        else:
            print("Valid")
