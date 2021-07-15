e,score_matrix=enumerate,lambda m:sum(c*(-1)**(i+j)for i,l in e(m)for j,c in e(l))
