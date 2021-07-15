def who_is_paying(name):
    names = [name]
    
    if len(name) > 2:
        truncated_name = name[:2]
        names.append(truncated_name)
    
    return names
