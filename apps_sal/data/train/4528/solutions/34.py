def my_languages(results):
    filtered_dict = {i: results[i] for i in results if results.get(i) >= 60}
    return sorted(filtered_dict, key=results.get, reverse=True)
