# DiscordNotify

Resends messages from Discord into telegram. Script resend attachments and tags username of the message author.
Bot supports any amount of Discord tokens, Discord channels and Telegram bots. Check config.

# How to use?

Configure config.
Bot uses "cfg.json" file as an entry point with all needed data.

1. Create copy of "cfg_example.json" and rename it into "cfg.json".
2. In cfg.json, fill the needed data:
- tg_botkey - auth token of telegram bot
- ds_token - auth token of discord account
- ds_channels - ids of discord channel u want to track messages in. Format: "channel_id": 0
- tg_chat - id of telegram chat, where the bot should send all fetched messages from discord channels
3. Save "cfg.json", run the bot with "python notifier.py"
4. You may add several ds_channels and several accounts.

# How to create bots, get tokens?

1. Telegram Bot
To create a telegram bot, DM https://t.me/BotFather and follow the instructions. 
After creating the bot, you will see such message:

![image](https://user-images.githubusercontent.com/109175575/190898213-39f9637e-bd93-4188-99b2-5fe04375cf14.png)

Copy bot auth token from the yellow box (under 'Use this token to access the HTTP API:'). Insert token into "tg_botkey" field in config.

2. Discord auth token
Login to your Discord account in browser. Press F12 to open inspect mode in your browser. In inspect mode, go to "Application". 
In "Application", select "Local Storage" and "https://discord.com". Find "token" key and copy its value.

![image](https://user-images.githubusercontent.com/109175575/190898428-afc2a4d6-c0dc-48ee-97e9-89116ba1ca61.png)

Insert copied token into "ds_token" field in config.

3. Discord channels IDs
Go to Discord user settings. Open "advanced" and turn on "developer mode".

![image](https://user-images.githubusercontent.com/109175575/190898483-243a6e18-667f-436b-a892-1dabe2a4be89.png)

Then right-click the channel you want to resend messages from and click "copy ID".

![image](https://user-images.githubusercontent.com/109175575/190898504-a45b5a1b-3a84-4c0b-8485-d2292c04b879.png)

Instert channel into config file.

4. TG Chat ID 
Insert any random number into tg chat id field in cfg.
Add the bot to the chat you want to send messages in (DM, group chat, channel (if channel grant bot with admin rights).
After adding the bot, send any message to the telegram channel, so the bot will see it.
Start the bot with "python notifier.py".
You will see the ID of the last channel where the bot fetched a message in console.

![image](https://user-images.githubusercontent.com/109175575/190898843-5f052556-8aa2-40df-9e92-a40f9c646881.png)

Copy ID and insert into config.

# Credits

[Original script] (https://github.com/karamelniycoder/discord-notifier_updated)
[Original script author] (https://github.com/karamelniycoder)
