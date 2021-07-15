def subcuboids(x,y,z):
    if (x*y*z)%2 == 0:
        return (((x + x**2)//2)*((y + y**2)//2)*((z + z**2)//2))
    else:
        return x*y*z*((x - (((1+x)//2) - 1))*(y - (((1+y)//2) - 1))*(z - (((1+z)//2) - 1)))
