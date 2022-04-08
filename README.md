# Random_Latin
基于Flask的一个博客自用的随机拉丁文返回api.仅供自家博客使用，没有任何优化。

语料来源于维基百科,知乎等.

演示:http://potassium.site/

## 主要功能
- 对每个请求返回一个随机的拉丁格言及翻译.
- 以`json`格式返回.
- 语料库来源于网络,明文形式存储在项目中.可自定义
## 示例
Fluid读取slogan的配置规范见https://fluid-dev.github.io/hexo-fluid-docs/guide/#slogan-%E6%89%93%E5%AD%97%E6%9C%BA

客户端使用`GET`方法访问URL并解析返回json结果.

```json
{
"content": "Forti nihil difficile \"力克万难\"\n",
"lines": 19,
"timestamp": 1649347413
}
```

## 部署方式
可以部署在任意位置,但要注意开放5000端口.或者通过修改源代码的方式自定义服务的端口.

常规部署:通过`virtualenv`进行部署.这种部署方式不能持续驻留后台,仅供测试用.

```bash
#./
virtualenv flask
flask/bin/pip install flask
chmod c+x random_latin.py
./random_latin.py
```

持久化部署:使用`pm2`配合常规部署方式实现持久化.最好根据自身路径检查修改.

编写`random_latin_config.yml`文件:

```yaml
# app.yml

name: random_latin #your-app-name-in-pm2
script: ./random_latin.py #/path/to/your/random_latin.py
interpreter: /path/to/repo/randomlatin/flask/bin/python3 #/path/to/flask_venv/bin/python
cwd: #/current/working/directory = /path/to/your/random_latin.py
# 配置了cwd之后, script和interpreter可以采取相对路径, pm2会自动的切换到cwd目录再执行启动应用的操作
```
然后使用下面的指令持久化部署:
```bash
pm2 start ./randomlatin/random_latin_config.yml
```
WARNING:最好使用绝对路径.

## Fluid下的配置修改
其余hexo主题请参考官方文档.
```yaml
index:
  slogan:
    enable: true
    text: api失效时显示该文字
    api:
      enable: true
      url: https://[your_ip_or_host]:5000/random_latin/
      method: "GET"
      headers: {}
      keys: ["content"]
```
## 注意

- 没有负载均衡,建议自己部署自己使用.如果qps过高可能会出现未预计的问题.
- 注意路径问题;必要时可以自己改路径,也可以编写脚本把路径切过去.



## 自定语料库
可以自行添加语料,在`Latin_Motto.txt`中.

每行载入一句,不能有空行或者奇怪的字符.

## 参考
http://www.pythondoc.com/flask-restful/first.html
https://cloud.tencent.com/developer/article/1181382
https://www.jianshu.com/p/67d888601a26