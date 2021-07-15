def merge(*dicts):
    merged = {}

    for dict in dicts:
      for key, value in dict.items():
        if key not in merged:
          merged[key] = [value]
        else:
          merged[key].append(value)
    return merged
