def my_languages(res):
    sorted_res = {k: v for k, v in sorted(list(res.items()), key=lambda item: item[1], reverse=True)}
    return [language for language, score in list(sorted_res.items()) if score >= 60]
        
            
    

