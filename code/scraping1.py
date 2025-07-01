import json
import re

# Surah name to number mapping (partial example, full list below)
surah_map = {
    'fatiha': 1,
    'baqarah': 2,
    'imran': 3,
    'an-nisa': 4,
    'maidah': 5,
    'al-anam': 6,
    'al-araf': 7,
    'al-anfal': 8,
    'taubah': 9,
    'yunus': 10,
    'hud': 11,
    'yusuf': 12,
    'rad': 13,
    'ibrahim': 14,
    'al-hijr': 15,
    'nahl': 16,
    'isra': 17,
    'kahf': 18,
    'maryam': 19,
    'taha': 20,
    'al-anbiya': 21,
    'al-hajj': 22,
    'al-muminun': 23,
    'nur': 24,
    'furqan': 25,
    'ash-shuara': 26,
    'naml': 27,
    'qasas': 28,
    'ankabut': 29,
    'rum': 30,
    'luqman': 31,
    'as-sajdah': 32,
    'ahzab': 33,
    'saba': 34,
    'fatir': 35,
    'yaseen': 36,
    'saffat': 37,
    'sad': 38,
    'zumar': 39,
    'ghafir': 40,
    'fussilat': 41,
    'shura': 42,
    'zukhruf': 43,
    'dukhan': 44,
    'jathiya': 45,
    'ahqaf': 46,
    'muhammad': 47,
    'fath': 48,
    'hujurat': 49,
    'qaf': 50,
    'dhariyat': 51,
    'tur': 52,
    'najm': 53,
    'qamar': 54,
    'ar-rahman': 55,
    'waqiah': 56,
    'hadid': 57,
    'mujadila': 58,
    'hashr': 59,
    'mumtahanah': 60,
    'as-saff': 61,
    'jumuah': 62,
    'munafiqun': 63,
    'at-taghabun': 64,
    'at-talaaq': 65,
    'tahrim': 66,
    'al-mulk': 67,
    'al-qalam': 68,
    'al-haqqah': 69,
    'maarij': 70,
    'nuh': 71,
    'jinn': 72,
    'muzzammil': 73,
    'muddaththir': 74,
    'qiyamah': 75,
    'al-insan': 76,
    'mursalat': 77,
    'naba': 78,
    'naziat': 79,
    'abasa': 80,
    'takwir': 81,
    'infitar': 82,
    'mutaffifin': 83,
    'inshiqaq': 84,
    'burooj': 85,
    'tariq': 86,
    'al-ala': 87,
    'al-ghashiyah': 88,
    'al-fajr': 89,
    'al-balad': 90,
    'ash-shams': 91,
    'al-lail': 92,
    'ad-duha': 93,
    'ash-sharh': 94,
    'at-tin': 95,
    'al-alaq': 96,
    'al-qadr': 97,
    'al-bayyinah': 98,
    'al-zalzalah': 99,
    'al-adiyat': 100,
    'qariah': 101,
    'at-takathur': 102,
    'al-asr': 103,
    'al-humazah': 104,
    'al-fil': 105,
    'quraish': 106,
    'al-maun': 107,
    'al-kawthar': 108,
    'al-kafirun': 109,
    'an-nasr': 110,
    'al-masad': 111,
    'ikhlas': 112,
    'al-falaq': 113,
    'an-nas': 114
}


input_file = "/home/nebulamind/Documents/AI Lab/Scraping/tags/merged_tags_output.json"
output_file = "/home/nebulamind/Documents/AI Lab/Scraping/tags/merged_tags_output_cleaned.json"

# Load input file
with open(input_file, 'r') as infile:
    data = json.load(infile)

# Process each ayah URL
for entry in data:
    ayah_ids = []
    for url in entry.get('ayah_urls', []):
        match = re.search(r'/surah-([^/]+)/ayat-(\d+)/', url)
        if match:
            surah_str = match.group(1).lower()
            ayah_no = match.group(2)
            surah_no = surah_map.get(surah_str)
            if surah_no:
                ayah_ids.append(f"{surah_no}|{ayah_no}")
            else:
                print(f"Warning: Surah name '{surah_str}' not found in map.")
    entry['ayah_ids'] = ayah_ids

# Save updated file
with open(output_file, 'w') as outfile:
    json.dump(data, outfile, indent=2)
