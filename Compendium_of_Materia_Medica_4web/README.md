Compendium_of_Materia_Medica_4web （本草纲目） 

# 简介 
了解本草纲目，输入本草纲目药物名，输出相关简，如：释名、气味、主治。操练Python语言开发练习：使用flask



## 输入：
用户输入本草纲目药物名
## 输出：
用户得到输出结果为：释名、气味、主治
## 从输入到输出，本组作品使用了：
### 模块
* [requests](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html#id2)
* [json](http://www.runoob.com/python/python-json.html)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)
* [time](https://docs.python.org/3/library/time.html)
### API
* [API](http://api.jisuapi.com/bencao/detail?appkey=bdc8ee0bb0227112&detailid=1&isdetailed=1)

* [API使用示例](https://www.jisuapi.com/api/bencao/)
### Web App动作描述

以下按web 请求（web request） - web 响应 时序说明

後端伺服器启动：执行 webapp_pick_a_medica.py 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

後端伺服器web 响应：webapp_pick_a_medica.py 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版templates/entry.html及一个含指标代码及名称的字典产出的产生《欢迎来到本草纲目》的HTML页面

前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"text"，变数名称(name)为'bencao_name'，详见HTML模版templates/entry.html

前端浏览器web 请求：用户选取指标後按了提交钮「开始」，则产生新的web 请求，按照form元素中定义的method='POST' action='/pick_a_medica'，以POST为方法，动作为/pick_a_medica的web 请求

後端服务器收到用户web 请求，匹配到@app.route('/pick_a_medica', methods=['POST'])的函数 pick_a_medica()

前端浏览器收到web 响应：模版中templates/results.html 的变数值正确的产生的话，前端浏览器会收到正确响应，看到指标的相关元数据。
## 作者成员：
见[_team_.tsv](_team_/_team_.tsv)
