# Telegram Screenshot Bot

Telegram bot that can take a screenshot of any website that you send the link to. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt 
```

## Structure
    
    ├── components              # Necessary components for the bot to operate
    │   ├── assets              # This folder stores all the screenshots of the page.
    │   ├── core.py             # Core.py consists of various functions for processing messages
    │   └── static_messages.py  # This file stores json all static messages sent by the bot to the user 
    ├── app.py                  # Executing file 
    └── config.py               # Config file that imports data from settings.ini file
    
## To run the bot in the console, write a command 
```bash
python app.py
```
