def look_and_say_and_sum(N):
    l=[1]
    for n in range(N-1):
        result = [1,l[0]]
        for i in range(1,len(l)):
            if l[i]==result[-1]:
                result[-2] += 1
            else:
                result += [1,l[i]] 
        l=result
    return sum(l)

