def my_parse_int(num_str):
  try:
    return int(num_str.strip())
  except:
    return 'NaN'
