
import json

import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demoLinebot.settings")
django.setup()
from line.models import Sticker
with open('stickers.json') as json_file:
    datas = json.load(json_file)
    for data in datas:
        packageId = data['packageId']
        stickerId = data['stickerId']
        url = data['stickerId']
        keywords = data.get('keywords',"")
        sticker,created = Sticker.objects.get_or_create(packageId = packageId ,stickerId = stickerId)  
        sticker.url = url
        sticker.keywords = keywords
        sticker.save()