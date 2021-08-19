def main():
    mod = (10**9 + 7)
    for i in range(eval(input())):
        printk = 0
        c = 0
        A, D = list(map(int, input().split()))
        aks = int(str(D) * A)
        s = (aks * aks)
        hey = str(s)
        for ii in hey:
            printk = printk + int(ii) * 23**c
            __ = int(ii) * printk
            c += 1
            # print __
            # print c
        ok_ = printk % mod
        print(ok_)


main()
