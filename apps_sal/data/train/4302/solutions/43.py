import numpy
def better_than_average(class_points, your_points):
    class_average = numpy.mean(class_points)
    if your_points > class_average:
        return True
    else: 
        return False

