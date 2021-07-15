rank_of_element=lambda a,i:sum(n<a[i]+(j<i)for j,n in enumerate(a))
