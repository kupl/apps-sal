def locate(seq, value):
    queue = [e for e in seq]
      
    while len(queue):
        el = queue.pop(0)
        if type(el) is list:
            queue = queue + el
        elif el == value:
            return True
    
    return False
