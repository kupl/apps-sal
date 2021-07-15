def string_to_array(s):
  return list(filter(lambda x : x , s.split(" "))) if s else [""]
