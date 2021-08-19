
n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))

    # 解説参照
    # 何度見ても解けない
    # どちらかは高橋君より良い
    # a<=bとする
    # a=b (1~a-1)*2
    # a<b c**2<abとする
    # c(c+1)>=ab？2c-2 / 2c-1

    if a == b:
        print((2 * a - 2))
    else:
        c = int((a * b)**(1 / 2))
        if c * c == a * b:
            c -= 1
        if c * c + c >= a * b:
            print((2 * c - 2))
        else:
            print((2 * c - 1))
