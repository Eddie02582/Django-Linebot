# Day2 

這篇教如何建立line bot,與其對應的試圖函數


## 建立 LINE Developers

前往<a href = "https://developers.line.biz/zh-hant/">LINE Developers</a>,點選登入並使用使用LINE帳號登入
會看到如下圖的畫面，輸入姓名及電子郵件即可，目的在於讓開發人員同意使用規範與聯絡使用

<img src="1.PNG" alt="Smiley face">



點選Creating a provider

## 建立Messaging API channel

點選Creating a Messaging API cHANNEL







## 在setting.py 新增

```
LINE_CHANNEL_ACCESS_TOKEN = 'Messaging API的Channel access token'
 
LINE_CHANNEL_SECRET = 'Basic settings的Channel Secret'
```


## install Ngrok

需要讓網址能夠公開(Public)且具有HTTPS，LINE頻道(Channel)才有辦法連結。

可以將LINE Bot應用程式(APP)部署到像Heroku，還可以使用Ngrok。Ngrok。是能夠將你本機的IP埠號(http://127.0.0.1:8000)，對應到一個隨機產生的HTTPS網址，並且這個HTTPS網址是對外公開的的，


## LINE Webhook URL
有了url 之後
