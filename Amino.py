import requests
import json
import websocket

class Amino:
    def __init__(self):
        pass
    def login(self, email=None, password=None, deviceid=None):
        headers={"NDCDEVICEID":deviceid,"NDC-MSG-SIG":"AWe7V9JF4yRIpQL1WhgoY6ZR9IXV","User-Agent":"Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G925F Build/MMB29K.G925FXXS4DPH8; com.narvii.amino.master/3.4.33563)"}
        data={"email":email,"secret":"0 "+password,"deviceID":deviceid}
        data=json.dumps(data)
        url="https://service.narvii.com/api/v1/g/s/auth/login"
        request=requests.post(url=url, headers=headers, data=data)
        response=json.loads(request.text)
        if response['api:message'] == "OK":
            self.sid="sid="+response['sid']
            self.userId=response['auid']
            self.deviceid=deviceid
            return response
            pass
        else:
            print ("Error!\n")
            print (response)
    def get_url_info(self, url=None):
        headers={}
        headers['NDCAUTH'] = self.sid
        headers['NDCDEVICEID'] = self.deviceid
        rurl=f"http://service.narvii.com/api/v1/g/s/link-resolution?q={url}"
        request=requests.get(url=rurl, headers=headers)
        response=json.loads(request.text)
        if response['api:message']=="OK":
            return response
            pass
        else:
            print (response)
            return response
    def join_vc(self, comId=None, chatId=None):
        headers={}
        headers['NDCAUTH'] = self.sid
        headers['NDCDEVICEID'] = self.deviceid
        websocket.enableTrace(True)
        ws=websocket.WebSocket()
        ws.connect("wss://ws1.narvii.com", header={"NDCAUTH":self.sid, "NDCDEVICEID":self.deviceid})
        data={
        "o":
        {
        "ndcId":comId,
        "threadId":chatId,
        "joinRole": 1,
        "id":2154531
        },
        "t":112
        }
        data=json.dumps(data)
        ws.send(data)
    def close_call(self):
        ws.close()