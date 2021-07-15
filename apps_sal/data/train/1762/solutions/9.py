class Line:
    def __init__(self,p1, p2):
        self.p1 = p1
        self.p2 = p2
    def printLine(self):
        print(("["+self.p1.printPoint()+","+self.p2.printPoint()+"] "))
        
class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        
    def printPoint(self):
        return "("+str(self.x)+","+ str(self.y)+")"

def get_my_key(line):
    firstX = line.p1.x
    secondX = line.p2.x
    if(firstX == secondX):
        return firstX+.1
    if firstX < secondX:
        return firstX
    else:
        return secondX
    
def rearrange(lines):
    for line in lines:
        if line.p1.y > line.p2.y:
            temp = line.p1.y
            line.p1.y = line.p2.y
            line.p2.y = temp
        if line.p1.x > line.p2.x:
            temp = line.p1.x
            line.p1.x = line.p2.x
            line.p2.x = temp
    return lines

def polygonArea(X, Y, n): 
    # Initialze area 
    area = 0.0
  
    # Calculate value of shoelace formula 
    j = n - 1
    for i in range(0,n): 
        area += (X[j] + X[i]) * (Y[j] - Y[i]) 
        j = i   # j is previous vertex to i 
      
  
    # Return absolute value 
    return int(abs(area / 2.0)) 
   
    
def mouse_path(s):
    length = len(s)
    xCoor = 0
    yCoor = 0
    point1 = Point(xCoor,yCoor)
    lines = []
    X = [0]
    Y = [0]
    direction = 1 #1 for right, 2 for left, 3 for up and 4 for down
    number = ""
    for i in range(length):
        if s[i] == 'L' or s[i] == 'R':
            if s[i] == 'L':
                if direction == 1:
                    direction = 3
                elif direction == 2:
                    direction = 4
                elif direction == 3:
                    direction = 2
                elif direction == 4:
                    direction = 1     
            else:
                if direction == 1:
                    direction = 4
                elif direction == 2:
                    direction = 3
                elif direction == 3:
                    direction = 1
                elif direction == 4:
                    direction = 2     
        else:
            number += s[i]
            if i+1 == length or s[i+1] == "L" or s[i+1] == "R":
                if direction == 1:
                    xCoor = xCoor + int(number)
                elif direction == 2:
                    xCoor = xCoor - int(number)
                elif direction == 3:
                    yCoor = yCoor + int(number)
                elif direction == 4:
                    yCoor = yCoor - int(number)
                point2 = Point(xCoor,yCoor)
                line = Line(point1,point2)
                X.append(xCoor)
                Y.append(yCoor)
                point1 = Point(point2.x,point2.y)
                lines.append(line)
                number = ""
               
    
    if lines[0].p1.x != lines[len(lines)-1].p2.x and lines[0].p1.y != lines[len(lines)-1].p2.y:
        return None
    if lines[0].p1.y == lines[len(lines)-1].p1.y and lines[0].p2.y == lines[len(lines)-1].p2.y:
        return None
    
    X.pop()
    Y.pop()
    lines.sort(key=get_my_key)
    lines = rearrange(lines)
    
    lines_copy = lines.copy()
    lines_entered = []
    
     
    #testing for intersects
    while len(lines_copy)>0:
        
        removeEntered = False
        line = lines_copy[0]
        for entLine in lines_entered:
                if entLine.p1.y == line.p1.y and entLine.p2.x > line.p1.x and line.p1.x != line.p2.x:
                    return None
                if entLine.p2.x < line.p1.x:
                    line = entLine
                    removeEntered = True
                    break
                    
        if removeEntered == True:
            lines_entered.remove(line)
            
        else:      
            if line.p1.x == line.p2.x:
                for entLine in lines_entered:
                    if entLine.p1.y > line.p1.y and entLine.p2.y < line.p2.y:
                        return None
                lines_copy.pop(0)
            else:
                    lines_entered.append(line)
                    lines_copy.pop(0)
                    
        removeEntered = False
        
        n = len(X)
    return polygonArea(X,Y,n)

    pass

