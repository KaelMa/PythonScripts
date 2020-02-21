 
import http.client
import hashlib
import urllib.parse
import random
import json
import os

#appid
appid = '20190709000316219'
#密钥
secretKey = '6DuUKo7ON0rLrb3NIbBL'

def getEnglish(input):
    '''
    调用百度翻译api，获取中文结果
    '''
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = input
    fromLang = 'zh'
    toLang = 'en'
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode('utf-8'))
    m2 = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+m2

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        #response是HTTPResponse对象
        response = httpClient.getresponse().read()
        res = json.loads(response)
        return res['trans_result'][0]['dst']

    except Exception:
        print(Exception)
        return 'error'
    finally:
        if httpClient:
            httpClient.close()

def rename(folder):
    '''
    重命名为英文
    '''
    for file in os.listdir(folder):
        absFile = os.path.join(folder,file)
        if (os.path.isfile(absFile)):
            name,subfix = os.path.splitext(file)
            newName = getEnglish(name)
            os.rename(absFile,os.path.join(folder,newName+subfix))
        else:
            rename(absFile)

# main
import sys
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('''
        please input file path.
        usage: python3 translate.py $(dest file path)
        ''')
        sys.exit()

    file = sys.argv[1]
    print(file)
    rename(file)
