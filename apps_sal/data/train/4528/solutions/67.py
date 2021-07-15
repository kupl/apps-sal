def my_languages(results):
    return list(
        map(lambda item: item[0],
        sorted(
            filter(lambda item: item[1] >= 60, results.items()),
            key=lambda item: item[1], 
            reverse=True)
        )
    )
