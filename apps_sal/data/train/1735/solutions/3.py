def shallowest_path(river):
    mx,my,crit=len(river[0]),len(river),lambda e:e[0]+len(e[1])
    M=[[(r[0]*mx*my,[(i,0)])]+[(99999*mx*my,[])]*(mx-1) for i,r in enumerate(river)]
    Q=set(((j,1),(i,0)) for i in range(my) for j in [i-1,i,i+1] if 0<=j<my and mx>1)
    while(Q):
      Q,R=set(),Q
      for (u,v),(i,j) in R:
          if crit(M[u][v])>max(M[i][j][0],river[u][v]*mx*my)+len(M[i][j][1])+1:
              M[u][v]=(max(M[i][j][0],river[u][v]*mx*my),M[i][j][1]+[(u,v)])
              Q.update(((a,b),(u,v)) for a in [u-1,u,u+1] for b in [v,v-1,v+1][a==u:] if 0<b<mx and 0<=a<my)
    return(min(M,key=lambda e:crit(e[-1]))[-1][1])
