# 判断变量的数据类型

可以使用type(var)来打印变量类型

使用isinstance(var,var_type)来判断变量类型

~~~objectivec
#cell is the data to tansform

if isinstance(cell,float):
  cell=int(float(cell))# float==>int
  str2+='%04d'%cell# int ===>str
if isinstance(cell,unicode):
  str2+=cell.encode('utf-8')
if isinstance(cell,str):
  str2+=cell
~~~

# 数据类型之间的转换

~~~objectivec
[python] 
int(x [,base ])         将x转换为一个整数    
long(x [,base ])        将x转换为一个长整数    
float(x )               将x转换到一个浮点数    
complex(real [,imag ])  创建一个复数    
str(x )                 将对象 x 转换为字符串    
repr(x )                将对象 x 转换为表达式字符串    
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象    
tuple(s )               将序列 s 转换为一个元组    
list(s )                将序列 s 转换为一个列表    
chr(x )                 将一个整数转换为一个字符    
unichr(x )              将一个整数转换为Unicode字符    
ord(x )                 将一个字符转换为它的整数值    
hex(x )                 将一个整数转换为一个十六进制字符串    
oct(x )                 将一个整数转换为一个八进制字符串    
~~~

# 格式化输出

~~~objectivec
str2+='%04d'%cell
~~~


~~~objectivec
今天写程序又记不清格式化输出细节了……= =索性整理一下。

python print格式化输出。

1. 打印字符串

print ("His name is %s"%("Aviad"))
效果：


2.打印整数

print ("He is %d years old"%(25))
效果：


3.打印浮点数

print ("His height is %f m"%(1.83))
效果：


4.打印浮点数（指定保留小数点位数）

print ("His height is %.2f m"%(1.83))
效果：


5.指定占位符宽度

print ("Name:%10s Age:%8d Height:%8.2f"%("Aviad",25,1.83))
效果：


6.指定占位符宽度（左对齐）

print ("Name:%-10s Age:%-8d Height:%-8.2f"%("Aviad",25,1.83))
效果：


7.指定占位符（只能用0当占位符？）

print ("Name:%-10s Age:%08d Height:%08.2f"%("Aviad",25,1.83))
效果：


8.科学计数法

format(0.0015,'.2e')
效果：


~~~

# 参考资料

- 1. http://www.cnblogs.com/plwang1990/p/3757549.html
- 2. https://github.com/urmyfaith/roadofios/blob/master/QuestionAndAnswer/xlsx2mdTable.py

