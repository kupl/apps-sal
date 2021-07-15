solve = lambda arr: list(reversed([{'Right': 'Left', 'Left': 'Right'}[arr[i + 1].split(' ')[0]] + ' ' + ' '.join(arr[i].split(' ')[1:]) if i < len(arr)-1 else 'Begin ' + ' '.join(arr[i].split(' ')[1:]) for i in range(len(arr))]))

