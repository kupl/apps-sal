def sum_times_tables(table,a,b):
    return(sum(list(map(lambda x: sum(list(map(lambda y: y * x ,range(a, b+1)))) , table))))
