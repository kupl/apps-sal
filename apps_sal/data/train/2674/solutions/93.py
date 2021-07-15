def two_sort(array):
  new_array = array
  new_array.sort()
  first_element = new_array[0]
  result = ""
  for i in range(len(first_element)):
    if i < len(first_element) - 1:
      result += first_element[i] + "***"
    else:
      result += first_element[i]
  return result    

