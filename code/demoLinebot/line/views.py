from django.conf import settings
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden)
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (ImageSendMessage, MessageEvent, StickerSendMessage,
                            TextSendMessage)

from .models import Sticker

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
 


 
@csrf_exempt
def callback(request):
 
    if request.method == 'POST':        
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        

        for event in events:             
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                if event.message.type=='text':  
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,                       
                        TextSendMessage(text=event.message.text)
                     )
               
                elif event.message.type=='sticker':# 如果有貼圖事件    
                    print (event.message)                 
                    stickerId,packageId = get_random()
                    line_bot_api.reply_message(  
                        event.reply_token,
                        StickerSendMessage(package_id=packageId, sticker_id=stickerId)
                    )                   
                    
                elif event.message.type=='image':
                    line_bot_api.reply_message(  
                        event.reply_token,
                        ImageSendMessage(
                            original_content_url = 'https://res.klook.com/image/upload/c_fill,w_960,h_460,f_auto/w_80,x_15,y_15,g_south_west,l_klook_water/activities/cmyvmrvbcil7awimgwt0.webp',
                            preview_image_url = 'https://res.klook.com/image/upload/c_fill,w_960,h_460,f_auto/w_80,x_15,y_15,g_south_west,l_klook_water/activities/cmyvmrvbcil7awimgwt0.webp'
                        )
                    )
                
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
   
def get_random():
    import random
    sticker = Sticker.objects.all()
    random_sticker = random.choice(sticker)
    
    return random_sticker.stickerId,random_sticker.packageId
   
   
        
def detect_object(path):
    import glob
    from pathlib import Path
    for svm_model in glob.glob("svm\\*.jpg"):
        name = Path(svm_model).stem
        detector = dlib.simple_object_detector(svm_model)
        
        img = cv2.imread(f, cv2.IMREAD_COLOR)
        dets = detector(img)
        if dets:
            return name
        
        # for index, face in enumerate(dets):     
            # left = face.left()
            # top = face.top()
            # right = face.right()
            # bottom = face.bottom()
            # cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
        
    
    
    
    
    
    
    
    
    