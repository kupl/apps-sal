def main():
    n = int(input())
    scores = []
    for i in range(n):
        a = list(map(int, input().split()))
        tot = sum(a)
        scores.append((-tot, i))
    scores.sort()
    for i in range(n):
        if scores[i][1] == 0:
            print(i + 1)


main()
