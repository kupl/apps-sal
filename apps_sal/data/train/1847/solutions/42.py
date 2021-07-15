class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle=rectangle
        self.pos=[]
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.pos.append([row1,col1,row2,col2,newValue])
        
        

    def getValue(self, row: int, col: int) -> int:
        if(len(self.pos)==0):
            return self.rectangle[row][col]
        else:
            t=-1
            for p in self.pos:
                row1,col1,row2,col2,val=p
                if((row>=row1 and row<=row2) and (col>=col1 and col<=col2)):
                    t=val
        if(t==-1):
            return self.rectangle[row][col]
        return t
                    
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

