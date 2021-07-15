def int32_to_ip(int32):
  return '.'.join([str(int(bin(int32)[2:].zfill(32)[i:i+8], 2)) for i in range(0, 32, 8)])
