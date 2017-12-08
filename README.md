# baidumap-miner
百度地图爬虫工具集；<br>
1.region-miner.html<br>
功能：获取国界线，省，市，县，区，街道行政界线<br>
使用方法：在第一个输入框中输入如“南京市”，然后按坐标按钮后，程序会在第二个输入框中输出界限坐标点集；每一行记录代表一个坐标，可以把坐标保存到文本编辑器中，然后导入到GIS软件使用即可<br>
注意事项：使用之前自己去百度地图api中心申请key，然后把第6行中的“你的百度地图key”换成你自己的key；程序获取的坐标是百度坐标系的，对wgs84有一定的偏移的<br>
2.coor-miner.html<br>
功能：百度坐标转成wgs84或者火星坐标系（cgcs2000）<br>
使用方法：在第一个输入框中输入你的百度坐标（一行一个坐标，经纬度用逗号分隔），选择相应坐标系后按转换按钮<br>
3.geocode-miner.py<br>
功能：地理编码<br>
使用方法：第7行中输入自己要的地物的名称，如“河海大学”，“江苏省人民医院”等，第8行中输入所在城市和你的百度地图key<br>
4.poi-miner.py<br>
功能：批量获取POI信息<br>
使用方法：city-ids.txt中写入自己所需要的城市信息（如果需要多个城市的话，可以按行写入多个城市信息，我预留了国内主要市县的信息了），然后32行中输入自己需要的POI名称，如 肯德基，电影院等等，可以一次搜索多个POI信息<br>
以上html工具都需要jquery，所以使用之前自己准备好jquery.js文件<br>
以上py工具都需要python3.*环境。无法在python2.7上运行<br>
