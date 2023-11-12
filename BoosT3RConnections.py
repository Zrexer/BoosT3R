import requests

class PoolConnections:
    
    def __init__(self,
                 url : str,
                 headers = {
                     'Content-Type' : 'Application/Json',
                     'Accept' : '*/*'
                 }
                 ) -> None:
        
        self.url = url
        self.head = headers
        
    def getConnectionJson(self):
        try:
            reqjg = requests.get(self.url, headers=self.head).json()
            return reqjg
        except Exception as GCJ:
            return GCJ
            pass
    
    def getConnectionStatus(self):
        try:
            reqsg = requests.get(self.url, headers=self.head).status_code
            return reqsg
        except Exception as GCS:
            return GCS
            pass
        
    def postConnectionJson(self):
        try:
            reqjp = requests.post(self.url, headers=self.head).json()
            return reqjp
        except Exception as PCJ:
            return PCJ
            pass
    
    def postConnectionStatus(self):
        try:
            reqsp = requests.post(self.url, headers=self.head).status_code
            return reqsp
        except Exception as PCS:
            return PCS
            pass
        
class AI:
    
    def chatGPT(text : str):
        
        try:
            req = str(dict(requests.get(f'https://haji-api.ir/Free-GPT3/?text={text}&key=hajiapi').json()).get('result').get('answer'))
            return req
        except Exception as ECH:
            return ECH
            pass
