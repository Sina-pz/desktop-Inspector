import os
# Cross-Platform
# Retrieves the names and paths of all files and folders (e.g., .lnk files, text files, images).
def list_desktop_icons():
    """List all desktop icons (files and folders) with their paths."""
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    print(f"Scanning desktop folder: {desktop_path}")

    icons = []
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        if os.path.isfile(item_path) or os.path.isdir(item_path):
            icons.append({"name": item, "path": item_path})
            print(f"Found: {item} -> {item_path}")

    return icons
