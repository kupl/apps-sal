def find_next_power(val, power):

  return int((val ** (1.0 / power)) + 1) ** power
