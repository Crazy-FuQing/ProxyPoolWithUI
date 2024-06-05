import re

html = '''
<style type="text/css">
</style>
</marquee>
<meta http-equiv="Content-Type" content="text/html; charset=GBK" />
<title>安小莫提示：匿名提取成功</title>
<script type="text/javascript">
var sogou_ad_id=768629;
var sogou_ad_height=90;
var sogou_ad_width=960;
</script>
<script>
var mediav_ad_pub = '47zFt2_1221523';
var mediav_ad_width = '640';
var mediav_ad_height = '60';
</script>

  	114.231.45.176:8089<br />
		178.33.26.119:80<br />
		123.30.151.66:8888<br />
		181.191.226.1:999<br />
		104.21.46.187:80<br />
		189.90.249.80:8090<br />
		203.28.9.235:80<br />
		190.97.238.82:999<br />
		177.73.68.150:8080<br />
		125.99.34.94:8080<br />
		35.182.7.190:443<br />
		52.210.25.181:8888<br />
		45.174.248.23:999<br />
		104.248.215.169:80<br />
		103.165.155.76:1111<br />
		67.226.222.2:80<br />
		115.29.148.215:10443<br />
		103.156.74.186:8080<br />
		104.129.198.250:8800<br />	</div>
<script type="text/javascript">
$(function(){
$('#adarea').slideDown(500);
$('#adclose').click(function(){
$('#adarea').slideUp(500);
});
});
</script>
<script type="text/javascript" src="http://www.66ip.cn/ggg/jquery.min.js"></script>
<div id="adarea"onclick=location.href='http://www.66daili.cn' style="cursor: pointer;display: none;position: fixed;right:15px;bottom:15px;width: 285px;height: 250px;background: url(http://www.66ip.cn/ggg/aaa.png) no-repeat;">
<div id="adclose" style="cursor: pointer; position: absolute;  top: 0px;  right: 0px;  display: block;  width: 20px;  height: 20px;font-family: cursive;background: url(http://www.66ip.cn/ggg/close.png) no-repeat;" title="点击关闭"> </div>
</div>
<script type="text/javascript">
$(function(){
$('#adarea').slideDown(500);
$('#adclose').click(function(){
$('#adarea').slideUp(500);
});
});
</script>
'''

# 使用正则表达式匹配 IP:Port 格式
pattern = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:(?P<port>\d+)'
matches = re.findall(pattern, html)

# 构造结果列表
result = [('http', match[0], int(match[1])) for match in matches]

# 打印结果
print(result)