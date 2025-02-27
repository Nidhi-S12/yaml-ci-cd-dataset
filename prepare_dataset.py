import os
import json

# Paths to dataset
faulty_dir = "datasets/faulty"
corrected_dir = "datasets/corrected"
output_file = "datasets/yaml_dataset.json"

dataset = []

# Loop through faulty YAMLs and get their corresponding corrected versions
for file in os.listdir(faulty_dir):
    faulty_path = os.path.join(faulty_dir, file)
    corrected_path = os.path.join(corrected_dir, file.replace("bad", "fixed"))

    # Read both files
    if os.path.exists(corrected_path):
        with open(faulty_path, "r", encoding="utf-8") as f1, open(corrected_path, "r", encoding="utf-8") as f2:
            dataset.append({
                "faulty_yaml": f1.read(),
                "corrected_yaml": f2.read()
            })

# Save as JSON
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(dataset, json_file, indent=4)

print(f"✅ Dataset saved to {output_file}")
