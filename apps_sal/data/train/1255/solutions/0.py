for _ in range(int(input())):
    s, k = map(str, input().split())
    k = int(k)
    n = "NOPE"
    al = [0] * 26
    for ele in s:
        al[ord(ele) - ord('a')] = 1
    l = len(s)
    ans = []
    for i in range(26):
        if len(ans) == l:
            break
        elif al[i] == 1 and k > 0:
            k -= 1
            ans.append(chr(i + ord('a')))
        elif al[i] == 0:
            ans.append(chr(i + ord('a')))

    if len(ans) != l:
        print(n)
    else:
        print("".join(ans))
