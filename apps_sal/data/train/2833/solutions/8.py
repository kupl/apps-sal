sect_sort=lambda arr,s,l=None: (lambda l: arr[:s]+sorted(arr[s:s+l])+arr[s+l:])(len(arr) if not l else l)
