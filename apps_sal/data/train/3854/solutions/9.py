def check_dates(A):
    Z=[0, 0, 0]
    for X in A:
        y0,m0,d0=map(int,X[0].split('-'))
        y1,m1,d1=map(int,X[1].split('-'))
        
        if y0<y1 and 12<d0 and 12<d1:Z[0]+=1    
        elif y0<y1 and m0==d0 and 12<d1:Z[0]+=1    
        elif y0<y1 and m0==d0 and m1==d1:Z[0]+=1    
        elif (m1==d1)and(12<m0 or 12<d0):Z[0]+=1    
        elif y0==y1 and m0==d0 and(12<m1 or 12<d1):Z[0]+=1   
        elif y0==y1 and m0==d0 and m1==d1:Z[0]+=1    
        elif y0==y1 and 12<d0 and 12<d1:Z[0]+=1
        elif y0==y1 and m0<=m1<d0<=12<d1:Z[0]+=1
        elif y0==y1 and m0<m1==d1<d0:Z[0]+=1
        elif y0==y1 and m0==d1<m1<d0:Z[0]+=1 
        elif y0==y1 and d1<m0<m1<=d0:Z[0]+=1                
        elif y0==y1 and d1<m0==d0<m1:Z[0]+=1    
        
        elif y0==y1 and (m0<=12<d0) and (m1<=12<d1):Z[1]+=1   
        elif y0==y1 and m1<=m0<=d1<=12<d0:Z[1]+=1     
        elif y0==y1 and d0<=m1<m0<=12<d1:Z[1]+=1     
        elif y0==y1 and d0<m1==d1<m0:Z[1]+=1    
        elif y0==y1 and d0==d1<m1<m0:Z[1]+=1        
        elif y0==y1 and m1<m0<d0==d1:Z[1]+=1    
        elif y0==y1 and m1<m0==d0<d1:Z[1]+=1   
        elif y0==y1 and m1<=m0<d1<d0:Z[1]+=1 
        elif y0==y1 and m1<d0<d1<=m0:Z[1]+=1
        elif y0==y1 and m1==d0<d1<m0:Z[1]+=1
        elif y0==y1 and d1<d0<m1<=m0:Z[1]+=1
        
        else:Z[2]+=1
    return Z
