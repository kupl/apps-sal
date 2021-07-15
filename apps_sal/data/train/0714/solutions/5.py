# cook your dish here
for testcase in range(int(input())):
    n = int(input())
    values = list(map(int, input().split()))
    
    current_total = sum(values)
    
    equality_value = current_total/n
    # lines 10-11 are ceil() function equivalent
    if equality_value>int(equality_value):equality_value+=1
    equality_value = int(equality_value)
    
    deviations = list()
    net_deviations = 0
    
    for value in values:
        deviation = value - equality_value
        deviations.append(deviation)
        net_deviations += deviation
        
    # print(current_total, equality_value, deviations, net_deviations)

    minimum_operations = abs(net_deviations)    # net_deviations has to be a negative value, using abs() just to be foolproof  
    
    for deviation in deviations:
        if deviation>0:minimum_operations += deviation
        
    print(minimum_operations)

