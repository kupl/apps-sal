def my_languages(results):
    ans = []
    sorted_results = sorted(results.items(), key=lambda k: k[1], reverse=True)
    print(sorted_results)
    for i in sorted_results:
        if i[1] >= 60:
            ans.append(i[0])
    return ans
