import json

def store_data(raw, enriched):
    with open("data.json", "w") as f:
        json.dump({"raw": raw, "enriched": enriched}, f, indent=2)
