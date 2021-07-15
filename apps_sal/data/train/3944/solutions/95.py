def sum_triangular_numbers(n):
    if n<0:
        return 0
    else:
        a = 2
        lst = []
        n = n-1
        while n>0:
            lst.append(a)
            a+=1
            n-=1
        print(lst)
        cnt = 1
        lst1 =[1]
        for i in range(len(lst)):
            cnt += lst[i]
            lst1.append(cnt)
        return sum(lst1)
            

