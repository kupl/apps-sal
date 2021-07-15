def opposite(number):
    convert = None
    if number < 0:
        convert = str(number)[1:]
    else:
      convert = '-' + str(number)
    try:
      return int(convert)
    except:
      return float(convert)
