check_generator=lambda g:{'GEN_CREATED':'Created','GEN_CLOSED':'Finished'}.get(__import__('inspect').getgeneratorstate(g),'Started')
