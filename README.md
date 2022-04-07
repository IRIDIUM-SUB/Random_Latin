# Random_Latin
基于Flask的一个博客自用的随机拉丁文返回api.仅供自家博客使用，没有任何优化。
语料来源于维基百科,知乎等.
# 概述
使用REST接口创建一个基于WSGI标准（PEP 3333）的很小的库.该接口通常都是服务于普通的HTTP请求,但是跟那些功能完整的网站相比,通常只需要处理数据.
# 主要功能
- 对每个请求返回一个随机的拉丁格言.
- 以`json`格式返回.
- 语料库来源于网络,明文形式存储在项目中.
# 注意
TODO:把5000端口开了
# CORS的解决
参考https://blog.csdn.net/lovebyz/article/details/52584551
# 返回格式
Fluid读取slogan的配置规范见https://fluid-dev.github.io/hexo-fluid-docs/guide/#slogan-%E6%89%93%E5%AD%97%E6%9C%BA

客户端使用`GET`方法访问URL并解析返回json结果.

设计的返回格式应为:
```json
{
    "status":"",
    "timestamp":"",
    "content":""
}
```
# yaml配置
```yaml
index:
  slogan:
    enable: true
    text: 这是一条 Slogan
    api:
      enable: true
      url: https://api.example.com/random_latin
      method: "GET"
      headers: {}
      keys: ["content"]
```