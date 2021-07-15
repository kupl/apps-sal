def gimme(array):
    for i in range(2):
      if (array[i] < array[i-1]) != (array[i] < array[i+1]):
        return i
    return 2
