def well(x):
    
    return 'Fail!' if x.count('good')==0 else 'Publish!' if x.count('good')<=2 else "I smell a series!"
