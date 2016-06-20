import requests
import json
import re
import codecs
from lxml import etree
from io import StringIO

master = requests.session()

#captcha
vcode_req = master.get('http://www.weihouqin.cn/captcha')
with open('/Users/X599/Desktop/WorkSpace/Python/weihouqinspider/cookies/vcode.jpg', 'wb') as f:
    f.write(master.get('http://www.weihouqin.cn/captcha').content)
vcode = input(u'input vcode:')

#_token
html = master.get('http://www.weihouqin.cn/login').text
gettoken = re.findall(r'_token: "([\w]*?)"', html)

#SigninData
SigninData = {
    'username': 600820,
    'password': 26292909,
    'captcha': vcode,
    '_token': gettoken[0]
}
url = 'http://www.weihouqin.cn/manage/work_orders'
getCookies = master.post('http://www.weihouqin.cn/postSignin', data=SigninData).cookies
work_orders = master.get(url, cookies = getCookies).text

#getjson
jsonData = {
    'keyword': '',
    'djyf': '',
    'clzt': '',
    'cxbm': '',
    'bxxm': '',
    'bxqy': '',
    'myd': '',
    'sbly': '',
    'page':1
}
query = master.post('http://www.weihouqin.cn/manage/work_orders/query', data = jsonData).json()

#json整理
json_str = json.dumps(query)
getjson = json.loads(json_str)
getfeedback = getjson['feedbacks']
getfeedbacks = str(getfeedback)
headerStart = "angular.module('SupportApp', ['ngMaterial']).config(function($mdThemingProvider){$mdThemingProvider.theme('altTheme').primaryPalette('purple');}).controller('SubheaderAppCtrl', function($scope){let None = 'none';$scope.messages =  "
headerEnd = ';});'
outputjs = str(headerStart + getfeedbacks + headerEnd).encode('utf-8')
with open('/Users/X599/Desktop/WorkSpace/Python/weihouqinspider/wwwroot/js/json.js', 'wb') as f:
    f.write(outputjs)
