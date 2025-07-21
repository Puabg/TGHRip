# TGHRip Bot - Deployment Guide

1. Clone the repository or unzip the project folder:
   git clone https://github.com/yourrepo/TGHRip.git

2. Enter the directory:
   cd TGHRip

3. Install required system packages (Ubuntu/Debian):
   sudo apt update && sudo apt install -y python3-pip ffmpeg

4. (Optional for DRM support) Install Wine + .NET for streamlink-drm on Linux:
   sudo apt install wine
   # Setup Wine environment for streamlink-drm if needed

5. Install Python dependencies:
   pip install -r requirements.txt

6. Setup Google Drive:
   - Enable Google Drive API in Google Cloud
   - Create a Service Account and download client_secrets.json
   - Place it inside /auth directory
   - Share your Google Drive folder with the service email

7. Set your config:
   - Edit config.ini and input your Telegram Bot Token, OwnerID, Group ID, etc.

8. Run the bot:
   python bot.py

Done! Your private DRM ripping bot should be running.

