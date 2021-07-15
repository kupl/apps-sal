def compare(s1,s2):
    return get_ascii_sum_value(s1) == get_ascii_sum_value(s2)
    
def get_ascii_sum_value(s):
    if s == None or len(s) == 0:
        return 0
    sum_value = 0
    for x in s:
      if not x.isalpha():
          sum_value = 0
          break
      else: 
          sum_value += ord(x.upper())
    return sum_value
