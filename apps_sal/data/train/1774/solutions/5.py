class Funnel(object):
    # Coding and coding...
    
    def __init__(self): 
        self.data = [[None]*i for i in range(1,6)]
        self.number_elements = 0
    
    def fill(self, *args):
        for new_elem in args:
            added = False
            if self.number_elements < 15:
                for row in self.data:
                    for i in range(len(row)):
                        if row[i] is None and not added:
                            row[i] = new_elem
                            added = True
                            self.number_elements += 1          
    
     
    def get_elem_above(self,row,idx):
        if row >= 5 or self.data[row][idx] is None:
            return []
        return [(row,idx)] + self.get_elem_above(row+1,idx) + self.get_elem_above(row+1,idx+1)
    
    def get_number_above(self,row,idx):
        return len(set(self.get_elem_above(row,idx)))
    
    def drip(self): 
        node = self.data[0][0]
        self.number_elements -= 1
        current_row = 0
        current_idx = 0
        while current_row <= 4 and self.data[current_row][current_idx] is not None:
            print(self.get_number_above(current_row+1,current_idx))
            print(self.get_number_above(current_row+1,current_idx+1))
            print(current_row,current_idx)
            if self.get_number_above(current_row+1,current_idx) >= self.get_number_above(current_row+1,current_idx+1):
                self.data[current_row][current_idx] = None if current_row == 4 else self.data[current_row+1][current_idx]
                current_row += 1
            else:
                self.data[current_row][current_idx] = None if current_row == 4 else self.data[current_row+1][current_idx+1]
                current_row += 1
                current_idx += 1

        return node
    
    def __str__(self): 
        res = ""
        for i,row in enumerate(self.data[::-1]):
            res += (" " * i + "\\" + " ".join([str(elem) if elem is not None else " " for elem in row]) + "/\n")
        return res[:-1]
