import requests

def send_wechat(msg):
    token = 'XXXXXXXXXXXX' #前边复制到那个token
    title = 'title1'
    content = msg
    url = 'http://www.pushplus.plus/send?token=' + token + '&title=' + title + '&content=' + content
    print(url)
    r = requests.get(url)
    print(r.text)

def send_wechat_all(msg):
    token = 'XXXXXXXXXXXX' #前边复制到那个token
    title = 'test notice title'
    content = msg
    topic = '1001'
    url = 'http://www.pushplus.plus/send?token=' + token + '&title=' + title + '&content=' + content + '&topic=' + topic
    print(url)
    r = requests.get(url)
    print(r.text)

if __name__ == '__main__':
#def start():
    #send_wechat('Life is short I use python')
    send_wechat_all('这里是测试1001')