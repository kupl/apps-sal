for _t in range(int(input())):
    n, k, d = list(map(int, input().split()))
    xs = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    my_x = 0
    my_l = 3 - ls[0]
    for x, l_ in zip(xs, ls):
        if l_ == my_l:
            if x <= my_x:
                print(x)
                break
            my_l = 3 - my_l
            my_x = max(x + 1, my_x + d)
        else:
            my_x = max(x + 1, my_x)
    else:
        print(k)
