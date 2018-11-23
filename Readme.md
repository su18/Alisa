## 给人类看的ReadMe

>  姓名：Alisa
>
>  年龄：7岁
>
>  性格：性情温和
>
>  技能：Web目录扫描
>
>  朋友：Elena（邻居）
>
>  家人：Curt（双胞胎哥哥）

Alisa是一个“*初升的太阳*”，不会太多的东西，也没见过什么市面

但是她带着**渴望**的眼睛来到这个世界，想要发光，照亮一片大地

她性格很好，见到你都会打招呼，不管出现什么*问题*，她都会跟你说清楚

Alisa经常与Curt争吵，究竟谁是父母最爱的孩子，也会常常因为拿不到扫描结果而自责

暖心的哥哥每次都会安慰她，带着她去一些**自己搭建的**没有防护的站逛逛，或者直接去“迪士尼”——**靶场**玩上一天

Elena是过了一段时间才搬进来的，两个人一拍即合，成为了最好的小伙伴

哥哥不在的时候，Alisa就会去找Elena一起玩，总是能在她那学会一些新知识

Alisa年纪还小，工作起来比较吃力，所以干什么都会比较慢

而不能长时间处于工作状态，在执行任务的过程中，她会找机会**休息一下**

Alisa很单纯，很活泼，希望她每天都能那么**开心**





## ReadMe For Programmer

AlisaWebDirScanner is a web directory discovery tool.By default it uses a dictionary based approach which is stored in ~/dict/ .

### Usage

-   -C  :  Customized cookies (e.g: key:value)
-   -P  :  Use http/https proxy (e.g: http://127.0.0.1:1080)
-   -T  :  Time delay between requests (e.g: 0.25 or 1.75)
-   -a  :  Customized UA (default Baidu-Spider UA)
-   -c  :  Crawl Depth(default 1)
-   -d  :  Dictionary list （e.g: php.txt,asp.txt,...default none)
-   -g  :  Discover sensitive dir by google hack
-   -t   :  Customized threads (default 5)
-   -u  :  Target url
-   -h  :  Help

Usage for instance

```shell
python3 alisa.py -u http://www.example.com -d php.txt -P http://127.0.0.1:1080 -g
```

### Features

Too lazy to write,see it yourself.

### Requirements

- request
- google

### Screenshots

Greeting

![image](https://github.com/JosephTribbianni/Alisa/raw/master/images/QQ%E6%88%AA%E5%9B%BE20181122150702.png)



Help

![](https://github.com/JosephTribbianni/Alisa/raw/master/images/QQ%E6%88%AA%E5%9B%BE20181122171653.png)



Scanning

![](https://github.com/JosephTribbianni/Alisa/raw/master/images/QQ%E6%88%AA%E5%9B%BE20181122183636.png)





