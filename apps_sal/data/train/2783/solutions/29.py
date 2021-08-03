import math
def get_grade(b, c, d): a = int((b + c + d) / 30); return'A'if a == 10else('F'if a < 6else chr(74 - a))
