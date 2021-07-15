import math

def tower_builder(n_floors, block_size):
    w, h = block_size
    stars = w #how many stars at first
    height_count = 0 #count for knowing when next floor
    tower = []    #result
    for i in range(n_floors*h): 
        ground_floor_stars = w*2*n_floors-w #gets how many stars in the bottom floor, intial width times two sides times floors minus width
        spaces = " " * int((ground_floor_stars - stars)/2) #calculates how many spaces for each floor for each side
        floor = spaces + '*'*stars + spaces
        tower.append(floor)
        height_count += 1
        if height_count == h:
            stars += w*2
            height_count = 0
    return tower
        



