import json

input_file = "/media/ubaisters/4CF2E61CF2E609D2/AI Lab/Scrapping_Quran/json/quranic_topics_and_references.json"
output_file = "/media/ubaisters/4CF2E61CF2E609D2/AI Lab/Scrapping_Quran/json/quranic_topics_and_references_cleaned.json"


# Load your original JSON file
with open(input_file, 'r') as infile:
    data = json.load(infile)

output = []

# Process each topic
for item in data:
    topic = item["Topic Title"]
    sub_topic = item["Sub-Topic"]
    verses = item["Verse References"].split(" ")

    for verse in verses:
        if ':' in verse:
            surah, ayah = verse.split(":")
            output.append({
                "Topic Title": topic,
                "Sub-Topic": sub_topic,
                "Verse ID": f"{surah}|{ayah}"
            })

        else:
            # Handle cases where verse format is not as expected
            print(f"Unexpected verse format: {verse}")

# Print or save the output JSON
# print(json.dumps(output, indent=2, ensure_ascii=False))

# Save to a new file
with open(output_file, 'w') as outfile:
    json.dump(output, outfile, indent=2)
