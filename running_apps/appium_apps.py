from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import AppiumOptions

def list_running_apps():
    """List all running applications using Appium."""
    # Define capabilities for the desktop session
    capabilities = {
        "platformName": "Windows",  # Use "mac" for macOS
        "automationName": "Windows",  # Specify automation framework
        "deviceName": "WindowsPC",
        # "app": "Slack"
        "app": "C:\\Users\\spashazanous\\AppData\\Local\\slack\\slack.exe"
        # "app": "Root"  # Attach to the desktop session
    }
    
    # Appium server URL
    appium_server_url = "http://localhost:4725" 

    # Connect to Appium server
    appium_options = AppiumOptions()
    appium_options.load_capabilities(capabilities)
    driver = webdriver.Remote(appium_server_url, options=appium_options)
    
    # Connect to the Appium server
    #driver = webdriver.Remote(command_executor=appium_server_url, desired_capabilities=capabilities)


    # Fetch all top-level windows (applications)
    windows = driver.find_elements(by=AppiumBy.XPATH, value="//*")

    print("Listing all running applications:")
    apps = []
    for window in windows:
        name = window.get_attribute("Name")
        rect = window.rect
        apps.append({
            "name": name,
            "coordinates": {
                "x": rect["x"],
                "y": rect["y"],
                "width": rect["width"],
                "height": rect["height"]
            }
        })
        # print(f"Application: {name}")
        # print(f"Coordinates: {rect}")
        # print("-" * 50)

    # Close Appium session
    driver.quit()
    return apps
