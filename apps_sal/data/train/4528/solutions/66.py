def my_languages(results):
    
    old=results.copy()
    for k,v in results.items():
        if v<60:
            old.pop(k) 
    new=sorted(old, key=old.get, reverse=True)
    return [i for i in new]
