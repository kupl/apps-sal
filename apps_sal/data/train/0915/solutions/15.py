for t in range(int(input())):
    n = int(input())
    numberlist = list(map(int, input().split()))
    print(len(list(set(numberlist))))
