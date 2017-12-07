import requests  
import json
import time
      
while True:  
    try:
        poiname = '河海大学'
        url2 = "http://api.map.baidu.com/geocoder/v2/?output=json&address="+poiname+"&city=南京市&ak=你的百度地图key"  
        resp2 = requests.get(url2)  
        resp2.encoding = 'utf-8'  
        baiduJson = json.loads(resp2.text)  
        if(baiduJson['status']!=0):
            print('API使用限制')
            continue  
        bLong = baiduJson['result']['location']['lng'] # 经度  
        bLat = baiduJson['result']['location']['lat'] # 纬度
        line = line.replace('\n','')
        print(str(bLong)+','+str(bLat)+'\n')  
        print('已获取'+poiname+'的数据\n')  
    except Exception as err:  
        print('ERR :: 获取'+poiname+'的数据时出错，一略过\n')  
        continue
    time.sleep(1)
file.close() 