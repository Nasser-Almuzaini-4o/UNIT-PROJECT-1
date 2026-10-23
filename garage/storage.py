import json
import os
import shutil
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "vehicles.json"


def load_data(path=DATA_FILE):
    """
   Reads all data from a JSON file and returns it as a dictionary.
    """
    path = Path(path)
    if not path.exists():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("JSON root must be an object")
        return data
    except ValueError:  
        backup = path.with_name(path.name + ".bak")
        shutil.copy(path, backup)
        print(f"Warning: {path.name} is corrupted. Backup saved as {backup.name}.")
        return {}


def save_data(data, path=DATA_FILE):
    """
     Writes all data to a JSON file.
     We first write to a temporary file and then replace the original,
     ensuring the file does not become corrupted if the program stops during the writing process.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, path)


def find_vehicle(plate, path=DATA_FILE):
    """Searches for a vehicle by its license plate number."""
    return load_data(path).get(plate)


def save_vehicle(vehicle, path=DATA_FILE):
    """Adds a new vehicle or updates an existing one (based on the license plate number), then saves the file."""
    data = load_data(path)
    data[vehicle["plate"]] = vehicle
    save_data(data, path)


def get_all_vehicles(path=DATA_FILE):
    """Returns all stored cars (dictionary: license plate -> car)."""
    return load_data(path)
