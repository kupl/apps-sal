from  math import sqrt



#Code recycled from my Kata solution
class Vector(object):

    __3DVECSIZE__= 3

    def __init__(self, *args, **kwargs):
        numArgs = len(args)
        
        if numArgs == 1:                            #Scenario: vecList is provided
            vecList = args[0]
        else:                                       #Scenario: a, b, c provided
            vecList = [args[0], args[1], args[2]]

        self.myVecSize = len(vecList)
        self.__checkForSizeException__(vecList)
        self.myComponents = vecList
        self.x = self.myComponents[0]
        self.y = self.myComponents[1]
        self.z = self.myComponents[2]
        self.magnitude = self.norm()
    #-----end constructor

    
    def __add__(self, v):
        return self.add(v)

    
    def __sub__(self, v):
        return self.subtract(v)

    
    def __eq__(self, v):
        return self.equals(v)

    
    def __str__(self):
        return self.toString('<','>')

    
    def __checkForSizeException__(self, v):
        lenPassedVec = len(v)
        if self.myVecSize != self.__3DVECSIZE__:
            raise ValueError('Missmatch of vector size: Size ', str(lenPassedVec), 'applied to vector of size ', str(self.myVecSize))  
        else:
            return lenPassedVec
    #-----end function


    def add(self, v):
        self.__checkForSizeException__(v.myComponents)
        return Vector([sum(x) for x in  zip(self.myComponents, v.myComponents)])
    #-----end function


    def subtract(self, v):
        negV = Vector([-comp for comp in v.myComponents])
        return self.add(negV)
    #-----end function

    
    #order of cross product is self cross v
    def cross(self, v):
        self.__checkForSizeException__(v.myComponents)
        xCrossComp = self.y*v.z - self.z*v.y
        yCrossComp = self.z*v.x - self.x*v.z
        zCrossComp = self.x*v.y - self.y*v.x
        return Vector([xCrossComp, yCrossComp, zCrossComp])
    #---end function

    
    def dot(self, v):
        self.__checkForSizeException__(v.myComponents)
        return (sum([ a*b for a,b in zip(self.myComponents, v.myComponents)]))
    #-----end function


    def norm(self):
        return sqrt( self.dot(self) )
    #-----end function


    def toString(self, groupSymbolLeft, groupSymbolRight):
        strVec = groupSymbolLeft
        for  i  in range(self.myVecSize-1):
            strVec += str(self.myComponents[i]) + ', '
        
        strVec += str(self.myComponents[-1]) + groupSymbolRight

        return strVec
    #-----end function

    
    def to_tuple(self):
        return tuple(self.myComponents)

    
    def equals(self, v):
        try:
            lenV = self.__checkForSizeException__(v.myComponents)
        except:
            return False 
        else:
            for i in range(lenV):
                if self.myComponents[i] != v.myComponents[i]:
                    return False
            return True
    #-----end function

#---end vector class

