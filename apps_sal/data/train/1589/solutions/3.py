T = int(input())

for testcase in range(T):
    i = 1
    above_30 = 0
    wsum_numerator = 0
    wsum_denominator = 0
    
    vals = [int(f) for f in input().split(" ")]
    
    val = vals[i-1]
    
    while not val == -1:
        if val > 30:
            above_30 += 1
        
        if val % 2 == 0:
            wsum_numerator += i * val
            wsum_denominator += i
        
        i += 1
        val = vals[i-1]
        
    wsum = wsum_numerator / wsum_denominator
    print(above_30, "{:.2f}".format(wsum))

