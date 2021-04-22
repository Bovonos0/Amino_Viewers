from __pycache__ import Amino
import os
import time
client=Amino.Amino()
print ('______________________________________________')
print ("By Bovonos")
time.sleep(0.5)
print ("Voice Chat Viewers Script")
time.sleep(0.5)
print ('______________________________________________')
time.sleep(1)
print ("")
emailsfolder=input ("Emails Folder:  ")
emails=open(emailsfolder, 'r')
password=input("Emails Password:  ")
deviceid=input("deviceId: ")
chatlink=input("Chat Link: ")
for email in emails:
    account=client.login(email=email,password=password, deviceid=deviceid)
    print (f"{email} loggining..{account['api:message']}")
    info=client.get_url_info(url=chatlink)
    comId=info['linkInfoV2']['path'][1:info['linkInfoV2']['path'].index('/')]
    chatId=info['linkInfoV2']['extensions']['linkInfo']['objectId']
    t=0
    try:
        client.join_vc(comId=comId, chatId=chatId)
        os.system("clear")
        t+=1
        print (t,"Done")
    except:
        print (t,"Faild")
        pass
print ("Done")
