bucket_of=lambda s:['air','water','slime','sludge'][(lambda x:('wet'in x or'water'in x or'wash'in x)+("i don't know"in x or'slime'in x)*2)(s.lower())]
