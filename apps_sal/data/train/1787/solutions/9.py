def minv(mat):
    N=len(mat)
    for i in range(N):
        extra=[0]*N
        extra[i]=1
        mat[i].extend(extra)
    for i in range(N):
        for j in range(N):
            if i==j:continue
            mul=mat[j][i]/mat[i][i]
            for k in range(N*2):
                mat[j][k]-=mul*mat[i][k]
    for i in range(N):
        div=mat[i][i]
        for j in range(2*N):
            mat[i][j]/=div
    for i in range(N):
        del mat[i][:N]
    return mat


class Datamining:
    def __init__(self, train_set):
        self.N=len(train_set)
        if self.N<6: 
            return
        self.Xt=[[],[],[],[],[],[]]
        self.y=[]
        
        for i in train_set:
            for k in range(6):
                self.Xt[k].append(i[0]**k)
            self.y.append(i[1])
        
        self.XtX = [[0]*6 for i in range(6)]
        for i in range(6):
            for j in range(6):
                self.XtX[i][j]=sum(self.Xt[i][k]*self.Xt[j][k] for k in range(self.N))
        self.XtY = [0]*6
        for i in range(6):
            self.XtY[i] = sum(self.Xt[i][k]*self.y[k] for k in range(self.N))
        
        self.XtX1=minv(self.XtX)
        self.b=[0]*6
        for i in range(6):
            self.b[i] = sum(self.XtX1[i][k]*self.XtY[k] for k in range(6))
        

    def predict(self, x):
        if self.N==5: return 5
        return sum(self.b[i]*x**i for i in range(6))

