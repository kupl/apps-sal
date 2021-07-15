def solve(arr):
    for i in arr:
        n=0
        for j in arr:
            n+=1
            if i+j ==0:
                break
            if len(arr)==n and i+j !=0:
                return i
