def my_languages(results):
    return sorted([result for result in results if results[result] >= 60],key=lambda x:results[x],reverse=True)
