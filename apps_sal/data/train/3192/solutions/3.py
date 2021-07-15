responses = [
  (lambda n: n < 11, "Hardly any"), 
  (lambda n: n < 51, "More than a handful!"), 
  (lambda n: n == 101, "101 DALMATIONS!!!"),
  (lambda n: True, "Woah that's a lot of dogs!")
]

how_many_dalmatians = lambda n: next(r for p, r in responses if p(n))
