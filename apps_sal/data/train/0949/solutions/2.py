from copy import copy


def main():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        i = 0
        l = []
        visited = [False for i in range(n)]
        for j in range(n):
            if not visited[j]:
                i = j
                s = 0
                while i < n:
                    visited[i] = True
                    if i + 1 < n and a[i] == a[i + 1]:
                        s += 1
                        i += 1
                    elif i + 2 < n and a[i] == a[i + 2]:
                        s += 1
                        i += 2
                    else:
                        break
                l.append(s)
        print(max(l))


main()
