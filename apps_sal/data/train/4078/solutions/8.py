first_n_smallest=lambda a,n:[v for _,v in sorted(sorted(enumerate(a),key=lambda x:x[1])[:n])]
