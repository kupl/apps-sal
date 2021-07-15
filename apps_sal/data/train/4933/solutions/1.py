In [20]: def random_case(x): return "".join([choice([c.lower(), c.upper()]) for c in x])  # That one                   
In [21]: %timeit random_case(s)                                                                                                 
834 ms ± 6.79 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [22]: def random_case(x): return "".join([choice([str.lower, str.upper])(c) for c in x])  # Mine                             
In [23]: %timeit random_case(s)                                                                                             
860 ms ± 3.77 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [26]: def random_case(x): return "".join([str.lower, str.upper][randrange(2)](c) for c in x)  # Blind4Basics
In [27]: %timeit random_case(s)                                                                                                  
931 ms ± 3.77 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

