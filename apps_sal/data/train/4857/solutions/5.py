def square_up(n):
    sqrList = [0 for _ in range(n*n)]

    #we build the square list, from right to left, in sets
    # e.g. for n==5  [5i-1,  5i-2,  5i-3,  5i-4, 5i-5]  for i = 1,2,...,n
    for i in range(1,n+1):          #iterate over the  1,2,...,n sets
        index = n*i - 1             #Start the index in the right most index of the set n
        for j in range(1, i+1):     #pattern: 1, 1;2, 1;2;3, 1;2;3;4, ..., 1;2;3;;;n 
            sqrList[index] = j
            index -=1

    return sqrList
#-----end function

