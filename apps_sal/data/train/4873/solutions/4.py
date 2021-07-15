import math

def distance_between_points(a, b):
    x_prime = b.x - a.x
    y_prime = b.y - a.y
    z_prime = b.z - a.z
    
    distance = math.sqrt(x_prime ** 2 + y_prime ** 2 + z_prime ** 2)
    return distance


