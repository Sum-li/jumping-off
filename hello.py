import requests
import re
def get_html(url):
    r1 = requests.get(url)
    return r1
def get_image(r1):
    res = r'src="(.+?\.jpg)" width'
    res1 = re.compile(res)
    imgs = res1.findall(r1.text)
   # img = requests.get(imgs)

    x = 0

   # with open('/home/lsgo28/PycharmProjects/a.jpg','wb') as f:
    for img in imgs:
        img = requests.get(img)
        filename = '/home/lsgo28/PycharmProjects/untitled123/' + str(x) + ".jpg"
        with open(filename, 'wb') as f:
            f.write(img.content)
        x += 1
print('图片获取中')
print('请输入url')
url = input()
if url:
    pass
else:
    print('没有输入url使用默认')
    url = 'http://tieba.baidu.com/p/1753935195'
print('正在获取网页')
r1 = get_html(url)
print('正在下载图片')
get_image(r1)
print('下载成功')