from desktop_icons.pywinauto_icons import list_desktop_pywin_icons
from desktop_icons.icons import list_desktop_icons
from running_apps.appium_apps import list_running_apps
from utils.permissions import ask_permission
from utils.output import save_output

def main():
    # print("Welcome to the Desktop Inspector!")
    # print("Choose an option:")
    # print("1. Inspect desktop icons (static)")
    # print("2. Inspect running applications (dynamic)")
    
    # choice = input("Enter your choice 1: desktop icons 2: running app ")
    # if choice == "1":
    #     # if ask_permission("access your desktop icons"):
    #         icons = list_desktop_pywin_icons()
    #         save_output("desktop_pywin_icons.json", icons)
    #     # else:
    #         # print("Permission denied for inspecting desktop icons.")
    # elif choice == "2":
        # if ask_permission("inspect running applications"):
    running_apps = list_running_apps()
    save_output("running_apps.json", running_apps)
        # else:
            # print("Permission denied for inspecting running applications.")

if __name__ == "__main__":
    main()
