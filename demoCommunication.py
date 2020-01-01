import requests
import random
import time
def createUsers(name: str):
    address = 'https://goldennumber.aiedu.msra.cn/api/NewUser?nickName=%s' % name
    r = requests.get(address)
    jsData = r.json()['userId']
    return jsData

def getRoundId(uuid: str, roomid):
    address = 'https://goldennumber.aiedu.msra.cn/api/State?uid=%s&roomid=%d' % (uuid, roomid)
    r = requests.get(address)
    return (r.json()['roundId'], r.json()['leftTime'])

def putData(uuid: str, roundId: str, n1, n2, hash):
    address = 'https://goldennumber.aiedu.msra.cn/api/Submit?uid=%s&rid=%s&n1=%d&n2=%d' % (uuid, roundId, n1, n2)
    if hash is not None:
        address += ('&token=%s' % hash)
    r = requests.post(address)
    return r.json()

def demoTry():
    # create user first
    uuid = createUsers('Py2-1')
    # get Round
    rid, leftTime = getRoundId(uuid, 1514)
    idx = 0
    while True:
        n1 = random.randint(0, 10)
        n2 = random.randint(11, 99)
        result = putData(uuid, rid, n1, n2, None)
        print('Idx[%d]' % idx, ': sent[%d][%d] with [%s] to [%s]' %(n1, n2, uuid, rid), result)
        if result == {}:
            time.sleep(leftTime)
        rid, leftTime = getRoundId(uuid, 1514)
        idx = idx + 1
        
