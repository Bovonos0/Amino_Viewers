import Amino
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
emails=open(emailsfolder).read().splitlines()
password=input("Emails Password:  ")
deviceid=input ("deviceID: ")
chatlink=input("Chat Link: ")
for email in emails:
    try:
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
    except:
        pass
print ("Done")
print ("""
Close Call?

 [1] Yes
 [2] No
 """)

close_the_call=input("choose: ")
if close_the_call=="1":
    os._exit(1)
elif close_the_call == "2":
    pass
else:
    print ("Not Found")