import requests

url = "https://oeis.org/A018819/b018819.txt"
html = requests.get(url)
a =[int(i) for i in html.text.split()[1::2]]

def make_sequences(n):
    try:
        return a[n]

    except Exception:
        return
