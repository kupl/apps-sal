def is_tune(notes):
    def is_in_key(a,b):
        major_scale_a = [(a+j) % 12 for j in (0,2,4,5,7,9,11)]
        return b%12 in major_scale_a
    return bool(notes) and any(all(is_in_key(i,n) for n in notes) for i in range(1,13))
