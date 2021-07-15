swap_head_tail=lambda a:(lambda m:a[-m:]+a[m:-m]+a[:m])(len(a)//2)
