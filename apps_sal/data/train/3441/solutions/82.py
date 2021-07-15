import numpy
import math

def get_average(marks):
    
    # raise NotImplementedError("TODO: get_average")
    # Faz a média do vetor 
    c = numpy.mean(marks)
    
    # Com a média, devolve o inteiro mais próximo arrendondado por decréscimo
    d = math.floor(c)
    
    return d
