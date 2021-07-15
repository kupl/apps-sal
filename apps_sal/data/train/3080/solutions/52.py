def who_is_paying(name):
    if len(name) > 2:    
        return [f"{name}" , f"{name[0]}{name[1]}"]
    else:
        return [f"{name}"]
