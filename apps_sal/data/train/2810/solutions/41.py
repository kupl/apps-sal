def solve(arr):
    letters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    count = 0
    cw = []
    
    for j in range(len(arr)):
        count = 0
        for i in range(len(arr[j])):
            if i > 24:
                break
            elif (arr[j][i]).lower() == letters[i]:
                count +=1
        cw = cw + [count]
    return cw
