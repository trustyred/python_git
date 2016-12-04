1.pycharm的使用

按住ctrl+鼠标左键可以查看某个方法或者库的源代码。
ctrl+‘/’可以进行注释

2.pythonic打开文件的方法
with open('path/to/file','r') as f:
  f.read()
表示在with所代表的作用域内f这个文件"句柄"，离开这个作用域的时候f就没用了。

3.yield

  具有yield的函数叫做生成器，生成器类型类似数据结构中的链表，但也不完全一样，一个大数据转化成为生成器类型将会非常的节省空间，使用那部分的时候才会占用空间，不使用的时候就不占用。
  yield的可以用来生成线程池，或者获得函数执行中的结果。

3.模块中的一些方法
  __doc__代表python文件中的说明文档一般用''' '''内的就是说明文档，__name__是用来表示当前的python环境是否是执行环境，而不是import进来的python文件，__file__存储的是当前执行环境的python文件的名字。

4.内建函数
  dir(),vars()两个作用差不多，可以理解为linux中命令的--help参数，只不过vars()查找的更详细，将所要查找的对象的属性与值的对应都显示出来，也就是以字典的形式显示出来。
  id(),type(),可以查看python中对象的两大重要属性，还有一个就是value，只要这三个相等，可以认为这两个对象是同一个对象。
  divmod(10，3)是计算两个相除后的商和余数。
  chr()，ord()。chr()是将编码以字符形式显示出来相当于解码，ord()是将字符以编码的形式显示出来，相当于编码。
  all(),any()。all()相当于对传入的iterable进行与运算，也就是说iterable如果全为True，结果就是True。any()对传入的iterable进行或运算，如果全为False结果才为False。
  format()是字符串格式化的另一种方式。s='{0} am a {1}' str=s.format('I','boy') 这时候str的结果就是I am a boy。
  apply()函数是执行函数的方法，s=apply(str,'abcd')。等价于s=str('abcd')
  map(),filter(),reduce()这三个方法很常用。map()将传入的函数作用于传入他的每个元素上，当你相对一个列表或其他的数据结构执行一个统一的方法时可以使用这个方法。filter()是一个过滤函数，传入他的函数的返回值要是bool类型,当将传入filter()的数据结构的对象进入函数的结果返回为False,就把这个对象过滤掉，最终的结果都是函数作用后结果为True的对象。reduce()有浓缩的意思，传入的函数一定要有两个参数，将传入reduce()的对象不断迭代传入那个函数。
  enumerate()函数枚举化传入的参数
  eval('8*8')相当于执行传入的字符串。

5.反射
  这是一个十分重要的概念用于以后的大型程序切换数据库的时候用。
  data_base='mysql'
  model=__import__(data_base)
  method='get'
  get=model.getattr(model,method)
  这样当数据库变更的时候我们可以很方便的更改。

6.常用模块
6.1random模块
random.random()			#获得小于1的一个随机数
random.randint(1,5)		#生成[1,5]的一个随机整数，注意是左闭右闭
random.randrange(1,5)	#生成[1,5)的一个随机整数，注意是左闭右开，比较符合python的风格。
应用场景1：
	生成验证码
6.2md5加密模块
import hashlib

hash=hashlib.md5		#选择hash的md5加密
hash.update('abcd')		#选择加密的字符串
print hash.hexdigest()	#以16进制的形式打印出来。

6.3(重点)
序列化和json
  pickle是python程序之间交互使用的一种格式，几乎可以序列化python中所有的数据结构，但pickle对人读是很不友好的。
  json是基本所有语言之间的序列化格式，但对python只能序列化基本的数据结构，json可读性好。
import pickle
l=[1,2,3,4]
dumped=pickle.dumps(l)		#在程序中的序列化
loaded=pickle.loads(dumped)	#在程序中的反序列化

l1=[4,5,6,7]
pickle.dump(l1,'d:\\a.txt')		#序列化的结果写入文件
pickle.load(open('d:\\a.txt'))	#从文件中读取并反序列化成pyton中的数据结构

6.4re模块
re.match('\w+','abcde123abc')	#match是包含开头的匹配，如果没有匹配到就返回none
re.search('\w+','67sdhjkk')		#search是全文匹配，只要找到一个就返回
re.findall('\w','asas')			#findall是找到全部的正则匹配到的串
r=re.complie('\d+')				#将你自己写好的正则传入上面三个函数时，他们都要编译一遍你的正则表达式，但是当调用函数次数很多的时候，每次都要编译一遍是很低效率的，你自己先编译一遍，将编译后的正则表达式传入就会快很多了。
re.group()						#将匹配到的一律返回
re.groups()						#只返回匹配到的组

6.5time模块
time.time()						#返回时间戳形式的时间,并且是当地时间
time.mktime(time.time())		#将一个结构化时间转化成时间戳时间

time.gmtime()					#返回一个UTC的结构化时间
time.localtime()				#返回本地的结构化时间
time.strptime('2014-11-11','%Y-%m-%d') #将一个自己输入的字符串时间转化成为结构化时间
time.strftime('%Y-%m-%d')		#默认返回的是本地时间

结构化时间是时间可以转化为其他任何其他形式的时间，想从时间戳转化成字符串需要先转化成结构化时间。
