print("🔥 test_path.py is running")

import os

filepath = "./mnt/data/martina_essays.jsonl"
print("📎 Type of filepath:", type(filepath))
print("📎 Value of filepath:", filepath)

try:
    with open(filepath, "r", encoding="utf-8") as f:
        print("✅ File opened successfully")
except Exception as e:
    print("❌ ERROR:", type(e), e)
