def abundant_number(num):
    # Your code here
        return sum([x for x in range(1,num) if num%x==0])>num
