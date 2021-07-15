def my_languages(results):
    resultsSorted = {key: value for key, value in sorted(list(results.items()), key=lambda item: item[1],reverse =True)}
    return [i for i  in resultsSorted if resultsSorted[i]>=60]

