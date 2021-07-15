def my_languages(results):
    lang=[]
    for key in list(results.keys()):
        if results[key] >= 60:
            lang.append({ "Key": key, "Value": results[key]})
    lang.sort(key=lambda x: x["Value"], reverse=True)
    return [l["Key"] for l in lang]
    
    

