import json
from pathlib import Path


def load_names(dataset_path: str) -> list[str]:
    dataset_path = Path(dataset_path)

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found at {dataset_path}")

    with open(dataset_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    names = data.get("names", [])
    names = [name.strip() for name in names if name.strip()]

    if not names:
        raise ValueError("No names found in dataset")

    return names
