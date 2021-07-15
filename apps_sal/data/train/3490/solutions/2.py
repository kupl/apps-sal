# This is O(n²), it's a bad solution
# You can do it in O(n*log(n)) but I'm too lazy for now
def array_manip(array):
    return [min(filter(lambda y: y > x, array[i+1:]), default=-1) for i,x in enumerate(array)]
