def fib_digits(n):
    numCount = [[0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6], [0,7], [0,8], [0,9]] # 2d array of the amounts of each number
    a,b = 1,1
    for i in range(n-1): # calculate the fibonacci number of the entered digit
      a,b = b,a+b
    fib_list = list(str(a)) # create a list of the numbers (in string form), one number per item
    i = 0
    while i < len(fib_list):
      numCount[int(fib_list[i])][0] += 1 # if number is x, the number of x's is incremented
      i+=1
    i = 0
    while i < len(numCount):
      numCount[i] = tuple(numCount[i]) # convert each list item to tuple
      if numCount[i][0] == 0:
        numCount.pop(i) # if there aren't any of a specific number, remove it
      else:
        i+=1
    return sorted(numCount, key=lambda x: (x[0], x[1]), reverse=True) # return the sorted list
