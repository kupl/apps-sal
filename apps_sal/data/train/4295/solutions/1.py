def balanced_num(number):
    number = [int(n) for n in str(number)]
    left, right = 0, 0
  
    while len(number) > 2 :
        left += number.pop(0)
        right += number.pop(-1)

    return "Balanced" if left == right else "Not Balanced"


