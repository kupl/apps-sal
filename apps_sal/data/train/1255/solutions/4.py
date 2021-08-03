# cook your dish here
alpha = "abcdefghijklmnopqrstuvwxyz"
for _ in range(int(input())):
    s, k = input().split()
    k = int(k)
    l = len(s)
    res = ''.join(sorted(s))
    if (26 - l) + k < l:
        print("NOPE")
    else:
        for i in alpha:
            if l == 0:
                break
            else:
                if i not in res:
                    print(i, end="")
                    l -= 1
                else:
                    if k != 0:
                        print(i, end="")
                        k -= 1
                        l -= 1
        print()
