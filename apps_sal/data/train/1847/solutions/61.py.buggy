class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        
        self.rows=len(rectangle)
        self.rectangle=rectangle
        if self.rows!=0:
              self.cols=len(rectangle[0])
        else:
             self.cols=0
                
                
    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        if row2>=row1 and col1<=col2 and row2<self.rows:
                        for i in range(row1,row2+1):
                                self.rectangle[i][col1:(col2+1)]=[newValue]*(col2-col1+1)
        else:
            print(\"Input Wrong\")
                
    def getValue(self, row: int, col: int) -> int:
        if row<self.rows and col<self.cols:
                row_select= self.rectangle[row]
                return(row_select[col])
        else:
            print(\"Input Wrong\") 


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
