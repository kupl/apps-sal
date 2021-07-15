def sort_me(arr):
    return [i[1] for i in sorted([[str(i),i] for i in arr],key=lambda i:i[0][-1])]
