def main():
    q = int(input())
    ans = []
    for i in range(q):
        n, k = map(int, input().split())
        s = input()
        min_ans = 10 ** 9
        pr1 = [0]
        pr2 = [0]
        pr3 = [0]
        for i in range(n):
            count1 = 0
            count2 = 0
            count3 = 0
            if i % 3 == 0:
                if s[i] != "R":
                    count1 += 1
                if s[i] != "G":
                    count2 += 1
                if s[i] != "B":
                    count3 += 1
            if i % 3 == 1:
                if s[i] != "G":
                    count1 += 1
                if s[i] != "B":
                    count2 += 1
                if s[i] != "R":
                    count3 += 1
            if i % 3 == 2:
                if s[i] != "B":
                    count1 += 1
                if s[i] != "R":
                    count2 += 1
                if s[i] != "G":
                    count3 += 1
            pr1.append(pr1[-1] + count1)
            pr2.append(pr2[-1] + count2)
            pr3.append(pr3[-1] + count3)
            j = i + 1
            if j >= k:
                count1 = pr1[j] - pr1[j - k]
                count2 = pr2[j] - pr2[j - k]
                count3 = pr3[j] - pr3[j - k]
                min_ans = min(min_ans, count1, count2, count3)
        ans.append(min_ans)
    print(*ans, sep="\n")


main()
