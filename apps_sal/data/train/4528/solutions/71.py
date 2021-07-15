def my_languages(R):
    return [k[0] for k in sorted(R.items(), key=lambda e: e[1], reverse = True ) if k[1]>=60]
