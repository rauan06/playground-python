from pytube import Search
import json

query = Search("Micheal Jackson")

results = []

for result in query.results:
    results.append({'title': result.title, 'link': result.watch_url})

with open("result.json", "w") as f:
    json.dump(results, f, indent=3, ensure_ascii=True, separators=(',', ':'))