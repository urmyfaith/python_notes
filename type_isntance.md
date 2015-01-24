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
