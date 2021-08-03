def my_languages(results): return [key for (key, val) in sorted(results.items(), key=lambda t: t[1], reverse=True) if val >= 60]
