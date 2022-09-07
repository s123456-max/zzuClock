import requests
from bs4 import BeautifulSoup
import re
import yagmail

# proxies = {
#     "http": "http://117.160.132.37:9091"
# }
obj = re.compile('parent.window.location="(?P<url>.*?)"', re.S)
obj1 = re.compile('失败', re.S)
obj2 = re.compile('<div style="width:100%;height:30px;"></div>(?P<success>.*?)onclick="window.location', re.S)
resp = requests.post('https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0', verify=False)
resp.encoding = 'utf8'
soup = BeautifulSoup(resp.text, "html.parser")
values = soup.find_all('input')
data = {
    'uid': os.environ["uid"],  # -------------------------------这里输入学号（必填）！
    'upw': os.environ["upw"],  # ---------------------------------这里输入密码（必填）！
    'smbtn': values[2]['value'],
    'hh28': values[3]['value']
}
resp = requests.post("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login", data=data, verify=False)
resp.encoding = 'utf8'
url = obj.search(resp.text).group('url')
resp = requests.get(url=url)
resp.encoding = 'utf8'
soup = BeautifulSoup(resp.text, "html.parser")
value = soup.find('iframe')
url = value['src']
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")
values = soup.find_all('input')
data = {
    'did': values[0]['value'],
    'door': values[1]['value'],
    'fun18': values[2]['value'],
    'sid': values[3]['value'],
    'men6': values[4]['value'],
    'ptopid': values[5]['value'],
    'sid': values[6]['value'],
}
resp = requests.post('https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb', data=data, verify=False)
resp.encoding = 'utf8'
soup = BeautifulSoup(resp.text, "html.parser")
values = soup.find_all('input')
img = soup.find('img')['src']
print(img)

# 这里是对验证码的提取（百度文字识别接口）
data = {
    'grant_type': 'client_credentials',
    'client_id': 'WNChcFVChONBFqX6xmrkMDMV',
    'client_secret': 'ou9XkXXPGQ5tIsqqhYFsrP0ZY0gch9dD'
}
resp = requests.post('https://aip.baidubce.com/oauth/2.0/token', data=data, verify=False)
access_token = resp.json()['access_token']
data = {
    'url': img
}
headers = {
    'content-type': 'application/x-www-form-urlencoded'
}
resp = requests.post('https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token='+access_token, data=data, headers=headers, verify=False)
print(resp.text)
results = resp.json()['words_result'][0]['words']
num_dict = {
    '零': 0,
    '壹': 1,
    '贰': 2,
    '叁': 3,
    '肆': 4,
    '伍': 5,
    '陆': 6,
    '柒': 7,
    '捌': 8,
    '玖': 9,
}
res = str(num_dict[results[0]]) + str(num_dict[results[1]]) + str(num_dict[results[2]]) + str(num_dict[results[3]])

data = {
    'myvs_94c': res,
    'myvs_1': '否',
    'myvs_2': '否',
    'myvs_3': '否',
    'myvs_4': '否',
    'myvs_5': '否',
    'myvs_7': '否',
    'myvs_8': '否',
    'myvs_11': '否',
    'myvs_12': '否',
    'myvs_13': '否',
    'myvs_15': '否',
    'myvs_13a': '41',  # 河南省
    'myvs_13b': '4106',  # 鹤壁市（郑州市：4101）
    'myvs_13c': '文化路97号',  # 街道
    'myvs_24': '否',  # 是否为当日返郑人员
    'memo22': '成功获取',
    'did': values[28]['value'],
    'door': values[29]['value'],
    'day6': values[30]['value'],
    'men6': values[31]['value'],
    'sheng6': values[32]['value'],
    'shi6': values[33]['value'],
    'fun118': values[34]['value'],
    'fun3': values[35]['value'],
    'jingdu': '114.20',  # 淇县的经度 正常值：values[36]['value']
    'weidu': '35.60',  # 淇县的纬度 正常值：values[37]['value']
    'ptopid': values[38]['value'],
    'sid': values[39]['value']
}
resp = requests.post("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb", data=data, verify=False)
resp.encoding = 'utf8'
soup = BeautifulSoup(resp.text, "html.parser")
if obj1.search(resp.text) is None:
    print('打卡成功！')
    yag = yagmail.SMTP(user='1586924294@qq.com', password='xrpalckormpjjijh', host='smtp.qq.com')
    contents = obj2.search(resp.text).group('success')
    yag.send(to=os.environ["email"], subject='zzuClock打卡成功！', contents=contents)
    yag.close()
    print('发送邮件成功！')
else:
    print('打卡失败！')
    print('失败原因：'+soup.find("li").text)
