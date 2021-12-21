import json
import PySimpleGUI as sg
import yaml
from urllib.parse import quote_plus, urlencode
import datetime
import re
import requests
from dateutil.easter import *
from plexapi.server import PlexServer
from plexapi import media, utils, settings, library
from plexapi.base import Playable, PlexPartialObject
from plexapi.exceptions import BadRequest, NotFound
from argparse import ArgumentParser
import os
import random
import shutil
import pathlib
from configparser import *

def update():
    with open('config.yml', 'r') as file:
        doc = yaml.load(file, Loader=yaml.SafeLoader)
        # Opening JSON file
        f = open(str(doc["Plex"]["Path"]))

    data = json.load(f)


    if data['Freq'][0] == 'Monthly':
        Date = datetime.date.today()
        Date.strftime("%b")
        session = requests.Session()
        session.verify = False
        requests.packages.urllib3.disable_warnings()
        plex = PlexServer(data['URL'], data['Token'], session, timeout=None)
        if data[Date] is none:
            Path = data['Default']
        else:
            Path = data[Date]
        prerolls = Path
        plex.settings.get('cinemaTrailersPrerollID').set(prerolls)
        plex.settings.save()
        print('Pre-roll updated')
    if data['Freq'][0] == 'Weekly':
        Date = datetime.date.today()
        Date.strftime("%Y-%m-%d")
        if data['WeekStart'] <= Date <= data['WeekEnd']:
            session = requests.Session()
            session.verify = False
            requests.packages.urllib3.disable_warnings()
            plex = PlexServer(data['URL'], data['Token'], session, timeout=None)
            prerolls = data['WeekPath']
            plex.settings.get('cinemaTrailersPrerollID').set(prerolls)
            plex.settings.save()
            print('Pre-roll updated')
        else:
            session = requests.Session()
            session.verify = False
            requests.packages.urllib3.disable_warnings()
            plex = PlexServer(data['URL'], data['Token'], session, timeout=None)
            prerolls = data['Default']
            plex.settings.get('cinemaTrailersPrerollID').set(prerolls)
            plex.settings.save()
            print('Pre-roll updated')
    if data['Freq'][0] == 'Daily':
        Date = datetime.date.today()
        Date.strftime("%a")
        session = requests.Session()
        session.verify = False
        requests.packages.urllib3.disable_warnings()
        plex = PlexServer(data['URL'], data['Token'], session, timeout=None)
        if data[Date] is none:
            Path = data['Default']
        else:
            Path = data[Date]
        prerolls = Path
        plex.settings.get('cinemaTrailersPrerollID').set(prerolls)
        plex.settings.save()
        print('Pre-roll updated')
    if data['Freq'][0] == 'Holiday':
        Date = datetime.date.today()
        Date.strftime("%Y-%m-%d")
        ThanksgivingDay = 22 + (10 - datetime.date(Date.year, 11, 1).weekday()) % 7
        # Valentines Day
        if Date.strftime("%b%d") == 'Feb14' and data['Valentines Day Enabled']:
            Path = data['Valentines Day']
        #April Fools
        elif Date.strftime("%b%d") == 'Apr01' and data['April Fools Enabled']:
            Path = data['April Fools']
        # Juy 4th
        elif Date.strftime("%b%d") == 'Jul04' and data['July 4th Enabled']:
            Path = data['July 4th']
        # Mardi Gras
        elif easter(Date.year) - datetime.timedelta(days=47) == Date and data['Mardi Gras Enabled']:
            Path = data['Mardi Gras']
        # Easter
        elif easter(Date.year) - datetime.timedelta(days=3) <= Date <= easter(Date.year) and data['Easter Enabled']:
            Path = data['Easter']
        # Halloween
        elif Date.strftime("%b") == "Oct" and int(Date.strftime("%d")) >= 23 and data['Halloween Enabled']:
            Path = data['Halloween']
        # Thanksgiving
        elif (datetime.date(Date.year,11,ThanksgivingDay) - datetime.timedelta(days=3) <= Date <= datetime.date(Date.year,11,ThanksgivingDay) + datetime.timedelta(days=4)) and data['Thanksgiving Enabled']:
            Path = data['Thanksgiving']
        # Christmas
        elif Date.strftime("%b") == "Dec" and int(Date.strftime("%d")) >= 20 and data['Christmas Enabled']:
            Path = data['Christmas']
        else:
            Path = data['Default']
        session = requests.Session()
        session.verify = False
        requests.packages.urllib3.disable_warnings()
        plex = PlexServer(data['URL'], data['Token'], session, timeout=None)
        prerolls = Path
        plex.settings.get('cinemaTrailersPrerollID').set(prerolls)
        plex.settings.save()
        print('Pre-roll updated')
    # Closing file
    f.close()
