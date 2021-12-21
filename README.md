# Plex-Automatic-Pre-roll-GUI
This is the new and improved Plex Automatic Pre-roll script with a GUI! It should be stable but if you find a bug please let me know


## Requirements
-[Python 3.7+](https://www.python.org/)
(Probably works on a lower version haven't tested)

-[PlexAPI](https://github.com/pkkid/python-plexapi)


## Installation
If you are on windows you can download the dist.zip file and run the excecutable. However you will still need to download the PrerollUpdate.py script if you want to have it update automatically in the background

First make sure you have Python installed version 3.7 and above. Next run:


```
pip install -r requirements.txt
```
That will install all the needed packages 

## Step by step instructions by Danny at smarthomepursuits.com

#Coming soon

## Settings
The config.yml file is created through the script automaitcally with no user input needed now. All changes are now made through the GUI YAY!


## Usage

### Setting Plex Preroll

You need to schedule a job for updating the preroll each day, week, or month depending how you want your pre-rolls updated.
You will now point this at the PrerollUpdate.py script 

**macOS or Linux:**
Ex: Monthly

```
crontab -e
0 0 * 1-12 * python /path/to/scripts/PrerollUpdate.py 2>&1
```

**Windows:**

Verify python is added to the PATH environmental variable
Search for task schedular and open it. Click "Create Basic Task" and enter a name and description. Then set the task to run monthly. Choose "Start a program" then for "Program/script" add the full path of the PrerollUpdate.py script Click "Finish" and you are done!


## Running For The First Time

The first time you run it you will see this:
![image](https://user-images.githubusercontent.com/75536101/146992593-a21866ea-7e3f-428c-8640-df197954819d.png)

Fill in all the fields for your plex IP and Token

How to get token: https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/ 

You can then setup a default pre-roll if you want or leave it blank

To set specific pre-roll fuctions select which type you want (Monthly, Weekly, Daily, Holiday), You will then see more fields on the right

Monthly:
![image](https://user-images.githubusercontent.com/75536101/146992956-baa1dd72-57e0-4aa2-bbdf-8cf4e75cd4be.png)

Weekly:
![image](https://user-images.githubusercontent.com/75536101/146993034-951f7bcc-6011-40a7-994b-1564cea961d1.png)

Daily:
![image](https://user-images.githubusercontent.com/75536101/146993063-d1dc0964-233c-4e11-8099-d5e9555b1497.png)

Holiday (If you want another holiday you can add that by using the weekly function and setting a date):
![image](https://user-images.githubusercontent.com/75536101/146993137-a99e4e79-0e4f-4348-b72a-6ffa19a370cc.png)

### Once you finish setting that up whatever you select in the Schedule section will be what the script will run on

For example in this photo

![image](https://user-images.githubusercontent.com/75536101/146993632-4decbe1e-d942-4c4a-b431-2bc68568f7c0.png)

I have selected Holiday and enabled the Christmas list therefore it will run through my Christmas list. If it does not find one enabled, finds empty strings, or does not match the holiday dates set in the system it will attempt to pull from the Default files.

I hope this is useful for some people and feel free to post any ideas or bugs
