from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(file("zipstips.html").read())
tipdivs = soup.findAll("div", attrs={"class": "single-tip"})
tips = []
for tip in tipdivs:
    dt = tip.text.split()[0].strip()
    title = tip.find(attrs={"class": "tip-label"}).text.strip('"')
    tiptxt = tip.find(attrs={"class": "tip"}).text
    print dt, title, tiptxt
    tips.append({"dt": dt, "title": title, "tiptxt": tiptxt})

json.dump(tips, file("tips.json", 'w'), indent=2)
