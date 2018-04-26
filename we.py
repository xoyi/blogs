# _*_ coding: utf-8 _*_
import re, json
import requests
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://fast.ishadowx.net/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

response = requests.get(url, headers=headers, verify=False, timeout=30).text
resp = re.findall(r'IP Address:<span .*?>(.*?)</span>.*?<span class="copybtn" .*?>'
                     r'.*?Port:<span .*?>(.*?)</span>.*?<span class="copybtn" .*?>'
                     r'.*?Password:<span .*?>(.*?)</span>.*?<span class="copybtn" .*?>', response, re.S)
res = random.sample(resp, 1)
for r in res:
    Address = r[0]
    Port = r[1].replace('\n', '')
    Password = r[2].replace('\n', '')
    print('*****抓取结果如下****：')
    print('%s \n%s \n%s' % (Address, Port, Password))
def get_configs():
    with open('gui-config.json', 'r') as con:
        conf = con.read()
        if conf != '':
            cf = json.loads(conf)
            config = cf.get('configs')[0]
            config['server'] = Address
            config['server_port'] = Port
            config['password'] = Password
            cfg = []
            cfg.append(config)
            cf['configs'] = cfg
            configs = json.dumps(cf)
            return configs
        else:
            pass
def write_configs():
    configs = get_configs()
    if configs != None:
        ff = open('gui-config.json', 'w')
        ff.write(configs)
        ff.close()
        print('******写入成功******')
    else:
        print('无数据写入')
write_configs()
input('Please enter the confirmation key to exit:')