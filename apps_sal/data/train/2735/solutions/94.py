def jumping_number(num):
    num = str(num)
    return ['Not!!',"Jumping!!"][all(abs(int(num[i+1]) - int(num[i])) == 1 for i in range(len(num)-1))]

