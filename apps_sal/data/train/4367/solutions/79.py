def area_or_perimeter(l, w):
    area = (l * w)
    perimeter = 2 * (l + w)
    if (l == w):
        return area
    else:
        return perimeter
    
#BDD
#Given length and width of a4-sided polygon
#Find the area or perimeter
#The polygon is a square or rectangle
#If it is a square then return its area
#If it is a rectangle then return its perimeter

#pseudocode 
#Funtion that takes in a parameter of l and w
#If square return Area
#If rectangle return Perimeter

