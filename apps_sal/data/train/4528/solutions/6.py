def my_languages(results):
    answer = []
    for k, v in results.items():
        if v >= 60:
            answer.append(k)
    return sorted(answer, key=lambda lang: results[lang], reverse=True)
