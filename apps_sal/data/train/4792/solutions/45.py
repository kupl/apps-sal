def parse_float(string):
 return None if any(i.isalpha() for i in string) else float(string)
