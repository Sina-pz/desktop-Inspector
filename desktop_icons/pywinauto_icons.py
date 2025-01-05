import json
from pywinauto import Desktop

def list_desktop_pywin_icons():
    """Retrieve all static icons (desktop apps/shortcuts) from the desktop."""
    try:
        desktop = Desktop(backend="uia")  # Access the desktop environment
        try:
            desktop_window = desktop.window(title="Desktop")
        except Exception as e:
            print(f"Could not find the desktop window: {e}")
            return []

        icons = desktop_window.children()  # Get all desktop icons

        print("Listing all desktop icons:")
        desktop_icons = []
        for icon in icons:
            name = icon.window_text()  # Get the caption or name of the icon
            rect = icon.rectangle()  # Get the coordinates of the icon
            desktop_icons.append({
                "name": name,
                "coordinates": {
                    "x": rect.left,
                    "y": rect.top,
                    "width": rect.width(),
                    "height": rect.height()
                }
            })
            # print(f"Icon: {name}")
            # print(f"Coordinates: {rect}")
            # print("-" * 50)

        return desktop_icons
    except Exception as e:
        print(f"An error occurred while listing desktop icons: {e}")
        return []