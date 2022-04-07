print("""
@Author:w01f
@repo:https://github.com/W01fh4cker/quark_download/
@version 1.0
@2022/4/7
___          ______          ___        ________         ____          _______
\  \        /  __  \        /  /      /   ____  \       |   |         /  ____/
 \  \      /  /  \  \      /  /       |  |   |  |       |   |     __/   /___
  \  \    /  /    \  \    /  /        |  |   |  |       |   |    /___   ___/
   \  \  /  /      \  \  /  /         |  |   |  |       |   |       |  |
    \  \/  /        \  \/  /          |  |___|  |       |   |       |  |
     \____/          \____/           \ ________/       |___|       |__|
""")
import json
import time
import requests
import os
url_wait = input("请输入您需要解析的和彩云网盘地址：")
password = input("请输入密码（没有就留空）：")
downpath = input("请输入您想要保存的绝对路径：")
def resolution_url_query():
    url_result = "http://www.52api.cc/caiyun/api.php?url=" + str(url_wait) + "&pwd=" + str(password)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
    }
    resp = requests.get(url=url_result,headers=headers)
    global res
    res = json.loads(resp.content.decode('utf-8'))
    code = res["code"]
    if(code==404):
        print("解析失败，请检查您的链接！")
    else:
        global download_url,filename,filesize
        download_url = res["file_download_url"]
        filename = res["file_name"]
        filesize = res["file_size"]
        if download_url is None:
            print("下载链接解析失败，请联系作者邮箱sharecat2022@gmail.com")
        else:
            print("下载文件名为：" + filename + "，下载文件大小为：" + filesize)
            IDMdownload(download_url,downpath,filename)

def IDMdownload(DownUrl, DownPath, FileName):
    NEWDownUrl =  DownUrl.replace('&','^&')
    IDMPath = r"" # 填入你的idm的绝对路径，例如C:\Users\Administrator\Desktop\IDM，确保底下有个应用叫IDMan.exe
    os.chdir(IDMPath)
    IDM = "IDMan.exe"
    command = ' '.join([IDM, '/d', NEWDownUrl, '/p', DownPath, '/f', FileName, '/a', '/s'])
    print(command)
    os.system(command)

if __name__ == '__main__':
    resolution_url_query()