import os

# Define dataset paths
faulty_dir = "datasets/faulty"
corrected_dir = "datasets/corrected"

# Ensure directories exist
os.makedirs(faulty_dir, exist_ok=True)
os.makedirs(corrected_dir, exist_ok=True)

# List of common YAML issues and fixes
yaml_pairs = [
    # 1. Missing colon
    (
        """name: CI Pipeline
on:
  push:
    branches:
      - main
jobs:
  build  # Missing colon
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
""",
        """name: CI Pipeline
on:
  push:
    branches:
      - main
jobs:
  build:  # Fixed missing colon
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
"""
    ),

    # 2. Incorrect indentation
    (
        """name: CI Pipeline
on:
  push:
    branches:
      - main
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
    uses: actions/checkout@v2  # Incorrect indentation
""",
        """name: CI Pipeline
on:
  push:
    branches:
      - main
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2  # Fixed indentation
"""
    )
]

# Generate 30 datasets by repeating and modifying patterns
for i in range(1, 31):
    faulty_yaml, corrected_yaml = yaml_pairs[i % len(yaml_pairs)]  # Cycle through pairs

    faulty_file = os.path.join(faulty_dir, f"bad_pipeline_{i}.yml")
    corrected_file = os.path.join(corrected_dir, f"fixed_pipeline_{i}.yml")

    # Force UTF-8 encoding to fix Unicode errors
    with open(faulty_file, "w", encoding="utf-8") as f:
        f.write(faulty_yaml)

    with open(corrected_file, "w", encoding="utf-8") as f:
        f.write(corrected_yaml)

print("✅ 30 YAML dataset pairs generated successfully!")
