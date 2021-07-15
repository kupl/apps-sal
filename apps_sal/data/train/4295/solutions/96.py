def balanced_num(number):
    print(number)
    if len(str(number))%2==0:
        lst = list(str(number))
        lst = list(map(int,lst))
        cnt = 0
        cnt1 = 0
        for i in range(len(lst)):
            if i <(len(lst)//2-1):
                cnt+=lst[i]
            elif i > (len(lst)//2):
                cnt1+=lst[i]
        print((cnt,cnt1))
        if cnt==cnt1:
            return "Balanced"
        else:
            return "Not Balanced"
    else:
        lst = list(str(number))
        lst = list(map(int,lst))
        cnt = 0
        cnt1 = 0
        for i in range(len(lst)):
            if i <len(lst)//2:
                cnt+= lst[i]
            elif i>len(lst)//2:
                cnt1+=lst[i]
        print((cnt,cnt1))
        if cnt==cnt1:
            return "Balanced"
        else:
            return "Not Balanced"

