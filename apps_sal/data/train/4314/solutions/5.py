chess_bishop_dream=lambda b,p,d,k:[(lambda q,r:[r,c-r-1][q%2])(*divmod(q+k*e,c))for c,q,e in zip(b,p,d)]
