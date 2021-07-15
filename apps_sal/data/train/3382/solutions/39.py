def lowercase_count(str):
    count = 0;
    alpha = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    trex = alpha.split(",")
    for x in str:
        if(x in trex):
            count += 1;
    return count;
