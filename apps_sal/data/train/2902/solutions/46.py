def opposite(number):
    if number >= 0:
        return float('-' + str(number))
    else:
        return float(str(number)[1:])
  # your solution here
