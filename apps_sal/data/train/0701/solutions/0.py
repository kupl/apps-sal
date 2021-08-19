# cook your dish here
def main():
    for _ in range(int(input())):
        N, k = [int(x) for x in input().split()]
        Powers = [k ** int(x) for x in input().split()]

        s1, s2 = 0, sum(Powers)

        ans = (0, None)

        i = 0
        while i < N - 1:
            s1 += Powers[i]
            s2 -= Powers[i]

            z = s1 * s2
            if z > ans[0]:
                ans = (z, i)
                # print(z)

            i += 1

        print(ans[1] + 1)


main()
