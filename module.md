## 模块使用及方法

[1 random](#1-random模块)

​	：可以生成随机浮点数、整数、字符串，以及随机选择列表序列中的一个元素，打乱一组数据等。

[2 time](#2-time模块)

[3 json](#3-json模块)



#### 1 random模块

- `random()`：返回[0,1]之间的随机数；
- `uniform(x,y)`：在[x,y)返回内，随机生成浮点数；
- `choice(seq)`：从序列seq(列表、元祖、字符串)中返回随机的元素；
- `getrandbits(n)`：a = nbit长度的值，返回[0,a]之间的整数；
- `shuffle(list)`：list序列从新排列；
- `randint(x,y)`：返回[x,y]之间的整数；
- `sample(seq,n)`：从seq序列中随机获取n个元素，组成列表(有n项)返回；
- `seed(n)`：n值随便设不设置，如果使用相同的seed( )值，则每次生成的随即数都相同，如果不设置这个       值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同；
- `randrange`([start,] stop [,step])：[start,stop)区间内以步长step随机返回值，只能返回整数；

```python 
import random
>>> uniform(2.5, 10.0)                   # Random float:  2.5 <= x < 10.0
3.1800146073117523

>>> choice(['win', 'lose', 'draw'])      # Single random element from a sequence
'draw'

>>> randrange(0, 5, 2)                 # Even integer from 0 to 100 inclusive
2									# 只能返回 0,2,4 整数

>>> deck = 'ace two three four'.split()
>>> shuffle(deck)                        # Shuffle a list
>>> deck
['four', 'two', 'ace', 'three']			#deck列表重新排列

>>> random.seed( 10 )
>>> random.random()
0.57140259469
>>> random.seed( 10 )
>>> random.random()
0.57140259469
>>> random.seed( 10 )
>>> random.random()					#生成同一个随机数，每次都要重新设置seek
0.57140259469

>>> random.getrandbits(2)			#2个bit，为3，所以随机返回[0,3]之间的整数
1								  # 0,1,2,3

>>> l1 = [1,2,3,4,5,6]				
>>> random.sample(l1,3)				#l1列表中随机返回长度为3的列表
[5, 2, 6]							#长度不可超过列表长度，长度为0，返回[]
```

#### 2 time模块

- `time()`：返回当前时间的时间戳；
- `localtime([secs])`：将一个时间戳转化为当前时区的时间元祖，secs参数未提供，则是当前时间戳；
- `gmtime([secs])`：将一个时间戳转换为UTC时区（0时区）的时间元祖；
- `mktime(t)`：将一个时间元祖转化为时间戳;
- `sleep(s)`：将线程推迟s秒时间运行；
- `asctime([t])`：把一个表示时间的元组表示为这种形式：'Sun Jun 20 23:21:05 1993'，如果没有参数，将会将当前时间的time.localtime()作为参数传入。
- `ctime([secs])`：把一个时间戳转化为：'Sun Jun 20 23:21:05 1993'的形式，如果参数未给或者为None的时候，将会默认以time.time()为参数。
- `strftime(format[,t])`：把一个时间元祖转化为格式化时间字符串，如果t未指定，将传入time.localtime()；
- `strptime(string,format)`：把一个格式化时间字符串转化为时间元祖,string与format要匹配；

```
格式化日期
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身

时间元祖内容：
#索引值(index)	属性(attribute)		     值(value)
#0	            tm_year(年)	            例如：2016
#1			   tm_mon(月)				1~12
#2			   tm_mday(日)				1~31
#3			   tm_hour(时)				0~23
#4			   tm_min(分)				0~59
#5			   tm_sec(秒)				0~60
#6			   tm_wday(星期几)		   0~6(0代表星期一)
#7			   tm_yday(一年中的第几天)	     1~366
#8			   tm_isdst(是否为夏令时)	 0，1，-1(-1代表夏令时)
```

```python
>>> import time
>>> time.localtime()
time.struct_time(tm_year=2018, tm_mon=1, tm_mday=31, tm_hour=10, tm_min=58, tm_sec=15, tm_wday=2, tm_yday=31, tm_isdst=0)
# tm_wday=2 表示周三

>>> time.mktime(time.localtime())
1517367612.0

>>> time.asctime()
'Wed Jan 31 11:01:37 2018'

>>> time.strftime('%Y-%m-%d %A %H:%M:%S')
'2018-01-31 Wednesday 11:03:24'

>>> time.strptime('2018-01-31 Wednesday 11:03:24','%Y-%m-%d %A %H:%M:%S')
time.struct_time(tm_year=2018, tm_mon=1, tm_mday=31, tm_hour=11, tm_min=3, tm_sec=24, tm_wday=2, tm_yday=31, tm_isdst=-1)
```

#### 3 json模块

- dumps(data)：把数据编码为JSON格式数据；
- `loads(JSON)`：解码JSON数据，返回python数据类型；
- `dump(data,file)`：把data数据编码为JSON格式数据，并存入file文件中；
- `load(file)`：把文件中的JSON数据转为python数据类型；

|  python对象   |   json对象   |
| :---------: | :--------: |
|    dict     |   object   |
| list, tuple |   array    |
|     str     |   string   |
| int, float  |   number   |
|    None     |    null    |
| True/False  | true/false |

```python
>>> import json
>>> data = {5: 6, 1: 2, 3: 4}
>>> json.dumps(data)
'{"5": 6, "1": 2, "3": 4}'

>>> j = '{"5": 6, "1": 2, "3": 4}'
>>> json.loads(j)
{'5': 6, '1': 2, '3': 4}

data = {5: 6, 1: 2, 3: 4}
with open('test.txt', 'w', encoding='utf8') as f:
    json.dump(data, f, indent=4, sort_keys=True)
    # indent 指定缩进， sort_keys 指定排序，True升序，False不变(默认)
test.txt:
{
    "1": 2,
    "3": 4,
    "5": 6
}

with open('test.txt', 'r') as f:
    print(json.load(f))
{'1': 2, '3': 4, '5': 6}
```

