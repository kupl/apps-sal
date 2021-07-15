expression_matter = lambda *a: [a[0]*a[1]*a[2],[(1+a[1])*a[2-2*(a[0]!=1)],(1+sorted(a)[1])*max(a)][a[1]==1],[sum(a),2*max(a)][a[1]==1],3][a.count(1)]
