def is_divisible(wall_length, pixel_size):
  return (wall_length / pixel_size).is_integer()
print(is_divisible(4050,27))
