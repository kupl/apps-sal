check_exam=lambda e,a:max(0,sum(4*(x==y)or-1for x,y in zip(e,a)if y))
