![Spotify Logo](https://raw.githubusercontent.com/RKgroupkg/Spotify-Downloader/refs/heads/Flac/IMG_20250204_135342_050.jpg)

# Spotify Downloader Bot

[live bot  @VibeTune_rkbot](https://t.me/VibeTune_rkbot)

## Introduction
> Yes, this repository is still maintained, and new features will be added over time.

## Common Issues

### Why are audio files not sending?
> Make sure that FFMpeg is installed! Check the logs for more details. See the image below to add FFMpeg if you are using Heroku.

![Add FFMpeg in Heroku](https://github.com/Masterolic/Spotify-Downloader/assets/93469093/0fbe0591-771a-460b-be69-3fb60536d44d)
![Add Python in Heroku](https://github.com/Masterolic/Spotify-Downloader/assets/93469093/6a0c1c9c-4c91-4bac-b6fb-0a40d5516e3c)

### Why do I get a 403 Forbidden error in my logs?
> Your VPS/Local Server might be blocked by YouTube. Try changing the IP address or using a proxy by filling the `FIXIE_SOCKS_HOST` variable, changing the location, or using cookies. Add this line ["cookiefile":"path"](https://github.com/Masterolic/Spotify-Downloader/blob/fe859965e62a5ca8f29fc69185cd132d456e4bfd/mbot/utils/mainhelper.py#L144) where `path` is defined as where your cookie file is. Refer [here](https://www.reddit.com/r/youtubedl/wiki/cookies/) for more details.


## Technical Details

### Which language and Telegram API are used?
> This bot is created using Python and the pyrogram library for Telegram.



## Deployment

### Easy way to deploy on Local/VPS
1. First, add variables in [config.env](https://github.com/Masterolic/Spotify-Downloader/blob/Latest/config.env):
   ```sh
   apt update && apt upgrade -y 
   apt install git ffmpeg python3 python3-pip -y
   git clone https://github.com/Masterolic/Spotify-Downloader.git 
   cd Spotify-Downloader/
   pip3 install -r requirements.txt 
   python3 -m mbot 
   ```

### Docker
1. Build and run the Docker image:
   ```sh
   docker build . -t musicbot
   docker run musicbot  
   ```



## Config Example
Add these variables in [config.env](https://github.com/Masterolic/Spotify-Downloader/blob/Latest/config.env):

### Required Environment Variables

### Get `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org) (required)
```sh
API_ID = ""
API_HASH = ""
```

### Your Telegram bot token (required)
```sh
BOT_TOKEN = ""
```

### ID of the owner of the bot (not username) (required)
```sh
OWNER_ID = ""
```
### Spotify Client Secret (get it from developers.spotify.com) (required)
```sh
SPOTIPY_CLIENT_SECRET = ""
```

### Spotify Client ID (get it from developers.spotify.com) (required)
```sh
SPOTIPY_CLIENT_ID = ""
```

### Optional Environment Variables

### Users with God permission (separate them with spaces) (optional)
```sh
SUDO_USERS = ""
```

### Chats that can use the bot (separate them with spaces) (optional)
```sh
AUTH_CHATS = ""
```

### Group ID for the log channel or leave it empty if not required (optional)
```sh
LOG_GROUP = ""
```


### Add your group ID for getting error log messages or leave it empty if not required (optional)
```sh
BUG = ""
```

### Get it from https://genius.com/developers (optional)
```sh
GENIUS_API = ""
```

### Temporary file storage path (optional)
```sh
XDG_CACHE_HOME = "~/.tmp"
```

### Paste your proxy URL here or leave it empty if not required (optional)
```sh
FIXIE_SOCKS_HOST = ""
```

### Pass `True` to make F_Sub enabled (default to `False`) (optional)
```sh
F_SUB = False
```

### Pass channel ID username or ID that starts with `-100` (optional)
```sh
F_SUB_CHANNEL_ID = ""
```

### Pass the invite link to the channel (e.g., `https://t.me/username` or `https://t.me/+jwjjwjw`) (optional)
```sh
F_SUB_CHANNEL_INVITE_LINK = ""
```

## Donation
> Please support me by buying me a pizza using the link below:
[Buy Me A Pizza](buymeacoffee.com/Rkgroup)

## Feedback
> Rate our bot [FEEDBACK](https://t.me/rkgroup_5316)

## About
> A Simple Open Source Spotify Downloader Bot for Telegram.

## Contact
> If you need any help or want to provide feedback, don't hesitate to contact me:

- [Instagram](https://www.instagram.com/rkgroup_5316?igsh=MXJiYWdxejhxZW11Mw==)
- [Telegram](https://t.me/rkgroup_5316)

<p align="center">
  <a href="https://t.me/Rkgroup_Bot">
    <img src="https://img.shields.io/static/v1?label=Join&message=Telegram%20Channel&color=blueviolet&style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Channel" />
  </a>
  <a href="https://telegram.me/Rkgroup_helpbot">
    <img src="https://img.shields.io/static/v1?label=Join&message=Telegram%20Group&color=blueviolet&style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Group" />
  </a>
</p>
