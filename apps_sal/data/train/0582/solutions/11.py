from sys import stdin, stdout


def main():
    t = input()
    t = int(t)
    while t:
        t = t - 1
        s = input()
        n = len(s)
        l = [0 for i in range(n)]
        l[n - 1] = -1
        q = []
        if s[n - 1] == ')':
            q.append(n - 1)
        for i in range(n - 2, -1, -1):
            if s[i] == ')':
                l[i] = l[i + 1]
                q.append(i)
            elif s[i] == '(' and len(q) == 0:
                l[i] = -1
            else:
                l[i] = q[len(q) - 1]
                q.pop()
        Q = int(input())
        arr = [int(x) for x in stdin.readline().split()]
        for i in range(Q):
            x = arr[i]
            x = x - 1
            if l[x] == -1:
                print(-1)
            else:
                print(l[x] + 1)


def __starting_point():
    main()


__starting_point()
