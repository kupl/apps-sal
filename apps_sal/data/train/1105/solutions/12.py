def main():
    t = int(input())
    while(t):
        n = int(input())
        list1 = list(map(int, input().split()))
        list1.sort(reverse=True)
        b0 = 0
        b1 = 0
        for i in list1:
            if b0 <= b1:
                b0 += i
            else:
                b1 += i
        print(max(b0, b1))
        t = t - 1


main()
