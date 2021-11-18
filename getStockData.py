import requests
import execjs
import js2py
import math
import time
import pandas as pd
code_list = []
def MCODE():
    jscode = '''
    function missjson(input) {  
        var keyStr = "ABCDEFGHIJKLMNOP" + "QRSTUVWXYZabcdef" + "ghijklmnopqrstuv"   + "wxyz0123456789+/" + "=";  
        var output = "";  
        var chr1, chr2, chr3 = "";  
        var enc1, enc2, enc3, enc4 = "";  
        var i = 0;  
        do {  
            chr1 = input.charCodeAt(i++);  
            chr2 = input.charCodeAt(i++);  
            chr3 = input.charCodeAt(i++);  
            enc1 = chr1 >> 2;  
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);  
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);  
            enc4 = chr3 & 63;  
            if (isNaN(chr2)) {  
                enc3 = enc4 = 64;  
            } else if (isNaN(chr3)) {  
                enc4 = 64;  
            }  
            output = output + keyStr.charAt(enc1) + keyStr.charAt(enc2)  
                    + keyStr.charAt(enc3) + keyStr.charAt(enc4);  
            chr1 = chr2 = chr3 = "";  
            enc1 = enc2 = enc3 = enc4 = "";  
        } while (i < input.length);  
    
        return output;  
    } 
    
    '''
    time1 = js2py.eval_js('Math.floor(new Date().getTime()/1000)')
    # py方式
    a = math.floor(time.time() / 1000)
    mcode = execjs.compile(jscode).call('missjson', '{a}'.format(a=time1))
    return mcode
def PageRquest(datetime, mcode):
    # 接口可以换
    url = 'http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1015'
    data = {
        'tdate': datetime, # 获取数据时间
        'scode': '399001'  # 股票代码 以及交易所简称
    }
    headers = {
        'mcode': str(mcode),
        'Referer': 'http://webapi.cninfo.com.cn/',
        'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1634795282; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1634799860',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }
    response = requests.post(url, headers=headers, data=data).json()
    code = response['records']
    for i in code:
        code_list.append(i)
def main(date):
    mcode = MCODE()
    PageRquest(date, mcode)
if __name__ == '__main__':
    # main()
    # 数据分析 pandas 自动化办公的
    datetime = pd.period_range('2021/5/1', '2021/10/20', freq='B')
    for date in datetime:
        main(date)
    df = pd.DataFrame(code_list)
    df.to_excel('code.xlsx')