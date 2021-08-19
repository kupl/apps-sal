def ranking(people):
    temp_result = sorted([item for item in people], key=lambda x: (-x['points'], x['name']))
    for (idx, item) in enumerate(temp_result):
        if idx and item['points'] == temp_result[idx - 1]['points']:
            item['position'] = temp_result[idx - 1]['position']
        else:
            item['position'] = idx + 1
    return temp_result
