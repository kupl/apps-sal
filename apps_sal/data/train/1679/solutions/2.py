# cook your dish here
def main():
    for _ in range(int(input())):
        n, k, x = map(int, input().split())
        if k == 1:
            for i in range(n):
                print(x, end=" ")
            print()
        else:
            def compxor(n):
                if n % 4 == 0:
                    return n
                if n % 4 == 1:
                    return 1
                if n % 4 == 2:
                    return n + 1
                return 0
            q = x ^ (compxor(k - 1))
# print(q)
            l = [i for i in range(1, k)]
            l.append(q)
# print(l)
            if n <= len(l):
                print(" ".join(map(str, l[:n])))
            else:
                j = 0
                for i in range(n):
                    print(l[j], end=" ")
                    if j == len(l) - 1:
                        j = 0
                    else:
                        j += 1
                print()


main()
