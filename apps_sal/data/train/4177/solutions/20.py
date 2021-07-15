def men_from_boys(arr):
    #Sorting the list
    arr.sort()
    print (arr)
    #since it has to start with the even, we will collect the even in an array called sorted
    sorted = []
    odds = []
    #Separating even from odds
    for num in arr:
      if num % 2 == 0:
          #making sure there are no dublicates
          if num not in sorted:
              sorted.append(num)
      else:
          if num not in odds:
              odds.append(num)
    #reversing the array with odds - since it is already sorted .reverse is enough
    odds.reverse()
    for numb in odds:
    #putting the odd numbers into the array of even
        sorted.append(numb)
    #returning the array
    return sorted

