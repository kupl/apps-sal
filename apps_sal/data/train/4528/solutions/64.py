my_languages = lambda results: [l for l in sorted(results, reverse=True, key=lambda a: results[a]) if results[l] >= 60]
