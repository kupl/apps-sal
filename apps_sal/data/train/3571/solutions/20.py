def is_divisible(wall_length, pixel_size):
    # Your code here.
    division_remainder=wall_length%pixel_size
    return division_remainder==0
    
    #& 
    #true_division!=float
    #need to divide wall length and pixel size. the true and floor division will not work, because there is 150.0.division that happens evenly can be represented with a decimal.So you need remainder. If there is a remainder, does not go in evenly, will be false.

