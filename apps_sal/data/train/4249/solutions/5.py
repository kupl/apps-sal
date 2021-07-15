abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def base64_to_base10(str, order=1):
  return base64_to_base10(str[:-1], order*64) + abc.index(str[-1]) * order if str else 0
