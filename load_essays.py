import json

def load_essay_corpus() -> list[str]:
    #print("🚨 Inside load_essay_corpus")

    # HARD CODE PATH – if this prints None, you're cursed
    filepath = "./mnt/data/martina_essays.jsonl"
    #print("📎 Filepath resolved as:", filepath)

    essays = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            if "completion" in data:
                essays.append(data["completion"].strip())

    #print(f"✅ Loaded {len(essays)} essays")
    return essays
