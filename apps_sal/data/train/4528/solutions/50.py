def my_languages(results):
    results = {k: v for k, v in sorted(list(results.items()), key=lambda item: item[1],reverse = True)}
    return [i for i in  list(results.keys()) if results[i]>=60  ]

