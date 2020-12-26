# coding: utf8
import requests
import os
from multiprocessing import Process

def downloadImg(img_url, fileLocation):
    print(img_url)
    proxies = {'http': 'http://localhost:9090', 'https': 'http://localhost:9090'}
    r = requests.get(img_url, proxies=proxies,verify=False,stream=True)
    fileName = img_url.split('/')[-1][:-1]
    print(fileName)
    print(r.status_code)  # 返回状态码
    if r.status_code == 200:
        open(os.path.join(fileLocation, fileName), 'wb').write(r.content)  # 将内容写入图片
    del r


def readUrl(fileName):
    urlFile = open(fileName)
    for url in urlFile.readlines():
        p = Process(target=downloadImg,args=(url,'dir'+fileName,))
        p.start()
        #downloadImg(url,'dir'+fileName)

if __name__ == '__main__':
    # 下载要的图片
    listFile = open('./list')
    for listLine in listFile.readlines():
        print(listLine[:-1])
        path = 'dir'+listLine[:-1]
        if not os.path.exists(path):
            os.mkdir(path)
        p = Process(target=readUrl,args=(listLine[:-1],))
        p.start()
