Start the Appium server:  appium --port 4725
Run your program: python main.py


pip install appium-python-client
Install Appium globally:  
  npm install -g appium
# driver it can be installed manually as well
  appium driver install --source=npm appium-windows-driver
  appium driver run windows install-wad
  pip install pywinauto

C:\Users\spashazanous\AppData\Local\Temp => search wind
search-ms:displayname=Search%20Results%20in%20Temp&crumb=System.Generic.String%3Awind&crumb=location:C%3A%5CUsers%5Cspashazanous%5CAppData%5CLocal%5CTemp

C:\Program Files (x86)\Windows Application Driver
C:\Users\spashazanous\.appium\node_modules\appium-windows-driver\scripts


Start the Appium server:  

  appium  or appium -allow-cors   or
  as th port in unavailable =>
appium --port 4725 --log-level debug
  The appium driver list confirms that the windows driver (version 3.1.3) is installed and ready for use. This is the correct driver for automating Windows applications using Appium.

The curl http://localhost:4723/status response indicates that the Appium server is running and ready to accept connections.


debugging :
powershell:

PS C:\Program Files (x86)\Windows Application Driver> .\WinAppDriver.exe
Windows Application Driver listening for requests at: http://127.0.0.1:4723/

Address 'http://127.0.0.1:4723/' is already in use

Failed to initialize: 0x80004005
PS C:\Program Files (x86)\Windows Application Driver> netstat -ano | findstr :4723
  TCP    0.0.0.0:4723           0.0.0.0:0              LISTENING       31368
 
 PS C:\Program Files (x86)\Windows Application Driver> tasklist | findstr 31368
node.exe                     31368 Console                    1     77,632 K
PS C:\Program Files (x86)\Windows Application Driver> taskkill /PID 31368 /F
SUCCESS: The process with PID 31368 has been terminated.

PS C:\Program Files (x86)\Windows Application Driver> .\WinAppDriver.exe
Windows Application Driver listening for requests at: http://127.0.0.1:4723/

as th port in unavailable =>

appium --port 4725 --log-level debug

  
////////
pip install pillow
Not installed yet:
 Appium Plugins
Enable advanced functionality such as image-based element finding.
Image Plugin:

Enables finding and interacting with UI elements based on their appearance (image recognition).
appium plugin install --source=npm appium-image-comparison-plugin


Event Listener Plugin
appium plugin install --source=npm appium-event-listener-plugin

Cache Interceptor:
Helps cache element locators to improve performance for large or complex apps.
appium plugin install --source=npm appium-element-cache-interceptor




pip install pillow
Requirement already satisfied: pillow in c:\users\spashazanous\appdata\local\programs\python\python312\lib\site-pack
ages (10.2.0)


Note:
Permission:

By Default: If the user is running the application, your application inherits the same permissions as the user account. This includes read access to files in the user’s Desktop folder.
Explicit Permission: It's always a good practice to ask for permission before accessing or processing user data, even if technically possible.
Display a Prompt: You can show a message asking for the user's consent to inspect the desktop folder.

