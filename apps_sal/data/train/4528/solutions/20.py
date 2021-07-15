my_languages = lambda results: [key for (key,val) in sorted(results.items(), key=lambda t: t[1], reverse=True) if val >= 60]
