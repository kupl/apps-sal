for i in range(int(input())):
    n = int(input())
    li_a = li_b = []
    for i in range(n):
        s = input()
        li_a.append(s.count('a'))
        li_b.append(s.count('b'))
    print(min(min(li_a), min(li_b)))
