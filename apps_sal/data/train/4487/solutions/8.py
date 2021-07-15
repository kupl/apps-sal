from collections import OrderedDict
def order_type(arr):
  res = OrderedDict([ 
          ("Constant", True),
          ("Increasing", True),
          ("Decreasing", True),
          ("Unsorted", True)
        ])

  def get_length(element):
    try:
      return len(element)
    except:
      return len(str(element))

  for first, second in zip(arr, arr[1:]):
    length_of_first = get_length(first)
    length_of_second = get_length(second)
    if length_of_first > length_of_second:
      res["Increasing"] = False
      res["Constant"] = False
    if length_of_first < length_of_second:
      res["Decreasing"] = False
      res["Constant"] = False
  for k in res:
    if res[k]:
      return k
