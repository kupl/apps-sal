i = __import__
wallpaper = lambda l, w, h, n=i('requests').get('https://num-words.com/in-words/0-9999/0-49/').text: [e.get_text() for e in i('bs4').BeautifulSoup(n)('b')][i('math').ceil((l + w) * 2 * h / 5.2 * 1.15) * 3 * bool(w * h * l)].lower()
