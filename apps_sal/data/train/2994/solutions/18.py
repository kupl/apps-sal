def find_digit(num, nth):
    if nth <=0 :
      return -1
    if num <0 :
      num = abs(num)
    if nth>len(str(num)):
      return 0
    else :
      strin = str(num)
      return int(strin[len(strin)-nth])
