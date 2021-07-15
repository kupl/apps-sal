from re import sub
def int32_to_ip(int32):
  return sub(r'(\d{8})', lambda x: str(int(x.group(), 2))+'.' , '{0:32b}'.format(int32).replace(' ', '0'))[:-1]
