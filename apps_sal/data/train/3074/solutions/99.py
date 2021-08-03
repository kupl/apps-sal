def growing_plant(up, down, desired):
    height = up
    count = 1
    while height < desired:
        height = height + up - down
        count += 1
    return count
