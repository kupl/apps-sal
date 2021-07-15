strange_coach=lambda a:(lambda c:''.join(k for k in sorted(c)if c[k]>4)or'forfeit')(__import__('collections').Counter(w[0]for w in a))
