# Axie Manager Bot
This is a Discord bot written in Python, with the purpose of helping our guild manage the scholars in our Discord server.
The purpose of this bot is that it can be used for guilds with multiple scholars and different managers, who each have their own scholars and wallets. 

# Features
## Commands
- !qr: Scholars can request their QR-code in the specified channel, default in '🤖┃login' channel. The bot will send them a private message containing their QR-code for login.
- !mute / !unmute: Mute and unmute specific users. Usage `!mute <@user>`, this gives a user the 'mute' role.
- !encrypt: Encrypt messages, necessary for encrypting private keys and storing them. Usage `!encrypt <message>`.
- !tryouts: Start tryouts, divides users with role 'tryout' in specific channels. More about this [below](#tryouts).
- !announce: Make announcements, using the bot as message sender. Usage `!announce <#channel>`, followed by a next `<text>`.
- !clear: Clear a number of messages. Usage `!clear <number>`, or `!clear <number> <@user>` to clear messages of specific user.
- !manager: Scholars can request information about their manager using this command. Only works if a scholar has manager assigned to them via a role.
- !leaderboard: Prints the leaderboard consisting of all scholars and ranked by MMR, also shows their average daily SLP income.
- !scholar: Adds a scholar to the database of scholars.
- !mydata: Scholar can request their up to date data, consisting of: in game slp, MMR, rank, payout day, and the number of days untill payout day.
- !help: Custom written `!help` command.

## Automation
- Automated alerts of axies specified in a Google Spreadsheet. More about this [below](#alerts).
- Automated buy, sell and listing alerts of other managers. These get posted in '🤝┃axie-trades' channel.
- Automated error handling. This sends all errors that occur in the '🐞┃bot-errors' channel, so every manager in the server is aware if there are any issues.

### Alerts
Setup:


### Tryouts
Tryouts are used to select a new scholar from a group of people (with the role 'tryout'). For each account that is available for a new scholar a new tryout group can be made, it is also possible to make less groups and pick the first and second best players.
Currenlty we let every tryout play for 3 hours on the account and after all tryouts are done the best will be picked. This is done by selecting the tryout that had the best winrate. At the moment the API for that is offline, so after a tryout is done they should send screenshots of their match history.

### Encryption
If you want to use the `!encrypt` function, you should have a fernet key. To generate this key use the following code:
```py
from cryptography.fernet import Fernet
print(Fernet.generate_key())
```
Save the printed key in the secret file (authentication.json).

### QR Code
The code of QRCodeBot.py and part of qr.py was written by [ZracheSs | xyZ](https://github.com/ZracheSs-xyZ), check out their repo for the original code.

## Dependencies
The required packages to run this code can be found in the `requirements.txt` file. To run this file, execute the following code block:
```
$ pip install -r requirements.txt 
```
Alternatively, you can install the required packages manually like this:
```
$ pip install <package>
```

## How to run
- Clone the repository and install dependencies as specified [above](#dependencies).
- Setup your own Discord bot, following this [tutorial](https://realpython.com/how-to-make-a-discord-bot-python/).
- Add your Discord bot token and your server name to authentication.json.
- Add your fernet key to authentication.json.
- Run `$ python src/main.py`
- See result
