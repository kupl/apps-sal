def winner(c):
    try:
        assert len(c) == 3 and all((0 < len(i['scores']) < 3 and all((not k % 5 and -1 < k < 101 for k in i['scores'])) for i in c if i['name'])) and (not all((sum(k['scores']) > 100 for k in c)))
    except:
        return False
    return max([[i['name'], sum(i['scores'])] for i in c], key=lambda x: x[1] < 101 and x[1])[0]
