def my_languages(results): return [l for l in sorted(results, reverse=True, key=lambda a: results[a]) if results[l] >= 60]
