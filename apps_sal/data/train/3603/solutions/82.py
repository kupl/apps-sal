#sample data (2,2)
#flower1 % 2 = even
#flower2 % 2 = even
#even != even is false

#(1,4)
#flower1 % 2 = odd
#flower2 % 2 = even
#odd != even is true

def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2
