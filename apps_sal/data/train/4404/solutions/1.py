def compare(s1, s2):
    s1 , s2 = s1.split('.') , s2.split('.')
    for i in range(abs(len(s1)-len(s2))): min(s1,s2,key = len).append('0')
    for num1 , num2 in zip(s1 , s2):
        num1 , num2 = int(num1) , int(num2)
        if num1 > num2: return 1
        elif num1 < num2: return -1
    return 0
