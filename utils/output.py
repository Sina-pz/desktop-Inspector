import json

def save_output(filename, data):
    """Save the given data to a JSON file."""
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data has been successfully saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving to {filename}: {e}")

