def is_tune(notes):
    return any(all((j+i)%12 in [0,2,4,5,7,9,11] for j in notes) for i in range(12)) if notes else False
