# reaction_time_game

## Set up GitHub Codespace using this repo

Welcome to your Python game development project! To avoid installation headaches on your local computer, we are using GitHub Codespaces. This gives you a powerful "clean slate" environment in the cloud where everything is already set up.

### Step 1: Launch Your Environment
Click the green `<> Code` button at the top of this page.

Select the Codespaces tab.

Click Create codespace on main.

Wait about 1–2 minutes for the "Building Container" process to finish. When you see the VS Code editor in your browser, you are ready!

### Step 2: Open Your Game "Monitor"
Because our code is running on a server in the cloud, it doesn't have a physical screen. We have to open a "Virtual Desktop" in your browser:

Look at the bottom of the screen and click on the PORTS tab.

Find the row for Port 6080 (labeled "desktop").

Hover over the Local Address for that port and click the browser icon (Open in Browser).

A new tab will open. Click the blue Connect button.

If it asks for a password, use: `vscode`

Keep this tab open! This is where you will see your game run.

### Step 3: Run Your Game
Go back to the VS Code tab and look at the Terminal at the bottom. Type these commands:

Connect to the virtual screen:

```
export DISPLAY=:1
```
(Note: You must run this command every time you open a new terminal window!)

Run your game script:

```
python main.py
```
See the results: Switch over to the browser tab you opened in Step 2. Your game window should be appearing there!

### Troubleshooting
The game window didn't pop up? Make sure you typed `export DISPLAY=:1` in the terminal before running your python command.

Connection Error on Port 6080? Wait a few seconds and refresh the page. Sometimes the virtual desktop takes a moment to start up after the Codespace builds.

Is the code laggy? Cloud-based gaming works best with a stable internet connection. If it feels slow, try closing other browser tabs you aren't using.

### Need Help?
If you get stuck, use the Live Share feature to invite your tutor to your session:

Click the Live Share icon in the left sidebar.

Click Share and send the link to your tutor.