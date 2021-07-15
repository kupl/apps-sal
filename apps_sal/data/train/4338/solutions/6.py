r=reversed;x=enumerate;reverse_on_diagonals=lambda m:[[f if i==j or len(m[i])-(i+j+1)==0 else m[i][j]for j,f in x(e)]for i,e in x([list(r(e))for e in r(m)])]
