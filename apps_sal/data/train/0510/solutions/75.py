def main():
    from bisect import bisect_left, bisect
    n = int(input())
    s = list(input())
    q = int(input())
    al = [[] for i in range(26)]
    for i in range(n):
        al[ord(s[i]) - 97].append(i)
    ans = []
    for i in range(q):
        a, b, x = input().split()
        if a == "1":
            al[ord(s[int(b) - 1]) - 97].pop(bisect_left(al[ord(s[int(b) - 1]) - 97], int(b) - 1))
            al[ord(x) - 97].insert(bisect_left(al[ord(x) - 97], int(b) - 1), int(b) - 1)
            s[int(b) - 1] = x
        elif a == "2":
            b = int(b) - 1
            x = int(x) - 1
            cou = 0
            for j in range(26):
                l = bisect_left(al[j], b)
                r = bisect(al[j], x)
                if l != r:
                    cou += 1
            ans.append(cou)
    for i in ans:
        print(i)


def __starting_point():
    main()


__starting_point()
