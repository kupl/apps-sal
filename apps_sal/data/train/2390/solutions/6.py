T = int(input())
test = 0
while test<T:
    
    N = int(input())
    
    arr = input()
    arr = [int(num) for num in arr.split(' ')]
    
    freq = {}
    
    for num in arr:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
          
    res = 0
    
    k = list(freq.values())
    k.sort(reverse=True)
    #print(k)
    m = max(k)
    
    idx = 0
    while m>0 and idx<len(k):
        m = min(m,k[idx])
        res += m
        m -= 1
        idx += 1
        
    print(res)
        
    test += 1
