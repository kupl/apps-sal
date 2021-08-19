def crosstable(players, results):
    count = len(players)
    pts = [sum(res[:i] + res[i + 1:]) for (res, i) in zip(results, range(count))]
    sb = [res[i] * pts[i] for res in results for i in range(count) if res[i] is not None]
    sb = [sum(sb[i * (count - 1):i * (count - 1) + count - 1]) for i in range(count)]
    (l_rank, l_pl) = (len(str(count)), len(max(players, key=len)))
    l_one_score = len(str(count))
    l_score = (l_one_score + 1) * count - 1
    (template_pts, template_sb) = (f'{{:.1f}}', f'{{:.2f}}')
    (l_pts, l_sb) = (max([len(template_pts.format(num)) for num in pts]), max([len(template_sb.format(num)) for num in sb]))
    row_len = l_rank + l_pl + l_score + l_pts + l_sb + 8
    template_rank = f'{{: >{l_rank}}}  '
    template = f'{{: <{l_pl}}}  {{: >{l_score}}}  '
    template_score = f'{{:>{l_pts}.1f}}  {{:>{l_sb}.2f}}'
    template_score_header = f'{{: ^{l_pts}}}  {{: ^{l_sb}}}'
    template_one_score = f'{{: >{l_one_score}}}'
    header = template_rank.format('#') + template.format('Player', ' '.join([template_one_score.format(i) for i in range(1, count + 1)])) + template_score_header.format('Pts', 'SB').rstrip() + '\n'
    delimiter = '=' * row_len + '\n'
    result = header + delimiter
    score = []
    for res in results:
        score.append([template_one_score.format(' ' if el is None else int(el) if el != 0.5 else '=') for el in res])
    list_sort = [dict(pts=pts[i], sb=sb[i], ind=i, name=players[i], res=score[i]) for i in range(count)]
    sort_pts = list(sorted(list_sort, key=lambda el: el['pts'], reverse=True))
    duplicate: bool = False
    start = 0
    for i in range(0, count):
        if not duplicate and i != count - 1 and (sort_pts[i + 1]['pts'] == sort_pts[i]['pts']):
            duplicate = True
            start = i
        elif duplicate and (i == count - 1 or sort_pts[i + 1]['pts'] != sort_pts[i]['pts']):
            sort_pts[start:i + 1] = sort_by_sb(list(sorted(sort_pts[start:i + 1], key=lambda el: el['sb'], reverse=True)), rank=start + 1)
            duplicate = False
            continue
        elif not duplicate:
            sort_pts[i]['rank'] = i + 1
    order = [rank['ind'] for rank in sort_pts]
    for rank in sort_pts:
        el = rank
        el['res'] = [el['res'][order[i]] for i in range(count)]
        s = template_rank.format(el['rank']) + template.format(el['name'], ' '.join(el['res'])) + template_score.format(el['pts'], el['sb']) + '\n'
        result += s
    return result.rstrip('\n')


def sort_by_sb(arr: list, rank: int):
    (duplicate, start) = (False, 0)
    for i in range(len(arr)):
        if not duplicate and i != len(arr) - 1 and (arr[i]['sb'] == arr[i + 1]['sb']):
            arr[i]['rank'] = ' '
            duplicate = True
            start = i
            rank_duplicate = rank
        elif duplicate and (i == len(arr) - 1 or arr[i]['sb'] != arr[i + 1]['sb']):
            arr[start:i + 1] = list(sorted(arr[start:i + 1], key=lambda el: el['name'].split(' ')[1]))
            for el in arr[start:i + 1]:
                el['rank'] = ' '
            arr[start]['rank'] = rank_duplicate
            duplicate = False
        else:
            arr[i]['rank'] = rank
        rank += 1
    return arr
