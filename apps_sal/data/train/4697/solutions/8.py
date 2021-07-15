common=lambda*a,c=__import__('collections').Counter:sum(__import__('functools').reduce(c.__and__,map(c,a)).elements())
