calculate_age = lambda b,c: ["You will be born in {} year{}.", "You were born this very year!", "You are {} year{} old."][((c-b)>=0) + ((c-b)>0)].format(abs(c-b), 's' if abs(c-b)!=1 else '')
