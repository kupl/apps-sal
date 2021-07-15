class Game():
    def ad_line(self,board):
        work=[[] for _ in range(board**2+1)]
        line_list=[[] for _ in range(2*board*(board+1)+1)]
        for i in range(1,board**2+1):
            numwork=((i-1)//board)*(2*board+1)
            numwork+=(i-1)%board+1
            work[i].append(numwork)    #top edge
            line_list[numwork].append(i)
            numwork+=board
            work[i].append(numwork)    #left edge
            work[i].append(numwork+1)  #right edge
            line_list[numwork].append(i)
            line_list[numwork+1].append(i)
            numwork+=board+1
            work[i].append(numwork)    #bottom edge
            line_list[numwork].append(i)
        return work,line_list
        
    
    def __init__(self, board):
        self.box=[0]*(board**2+1)
        work=self.ad_line(board)
        self.box_line=work[0]
        self.line_list=work[1]

    def play(self, lines):
        out=lines[:]
        work_next=[]
        for line in lines:
            for box in self.line_list[line]:
                self.box[box]+=1
                if self.box[box]==3 : work_next.append(box)
        while work_next:
            box=work_next.pop(0)
            for line in self.box_line[box]:
                if line in out : continue
                out.append(line)
                for n_box in self.line_list[line]:
                    self.box[n_box]+=1
                    if self.box[n_box]==3 : work_next.append(n_box)
        return sorted(out)
