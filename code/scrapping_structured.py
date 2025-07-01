import json

input_file = "/home/nebulamind/Documents/AI Lab/Scraping/tags/quranic_topics_and_references.json"
output_file = "/home/nebulamind/Documents/AI Lab/Scraping/tags/quranic_topics_and_references_cleaned.json"
# Load your original JSON file
with open(input_file, 'r') as infile:
    data = json.load(infile)

flattened = []

for entry in data:
    topic = entry.get("Topic Title", "")
    sub_topic = entry.get("Sub-Topic", "")
    verse_refs = entry.get("Verse References", "")
    
    for verse in verse_refs.split():
        if ':' in verse:
            parts = verse.split(":")
            if len(parts) == 2:
                surah, ayah = parts
                flattened.append({
                    "Topic Title": topic,
                    "Sub-Topic": sub_topic,
                    "Verse Reference": f"{surah}|{ayah}"
                })
            else:
                print(f"Skipping malformed verse (too many colons): {verse}")
        else:
            print(f"Skipping malformed verse (no colon): {verse}")

# Save to a new file
with open(output_file, 'w') as outfile:
    json.dump(flattened, outfile, indent=2)
