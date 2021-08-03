def is_divisible(wall_length, pixel_size):
    # Your code here.
    return wall_length % pixel_size == 0


print(is_divisible(3, 5))
print(is_divisible(8, 4))
