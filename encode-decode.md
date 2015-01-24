# 字符串和unicode

**字符串是unicode进行编码(encode)得到的**(多读几遍,字符串是怎么来的)

~~~objectivec
 str ---decode---> unicode
 
 unicode ----encode---> str
~~~


**字符串进行解码(decode)**得到unicode.

字符串使用引号包含,unicode前面有一个u

~~~objectivec
'hello'  ==> 字符串
u'hello' ===>unicode
~~~

## str解码方法decode

方法1.

~~~objectivec
>>> s = unicode('中文', 'utf-8')
>>> s
u'\u4e2d\u6587'
~~~

方法2.

~~~objectivec
 >>> ('中文').decode('utf-8')
u'\u4e2d\u6587'
~~~


## unicode编码为str(encode)

~~~objectivec
>>> u'中文'.encode('utf-8')
'\xe4\xb8\xad\xe6\x96\x87'
>>> type(u'中文'.encode('utf-8'))
<type 'str'>
~~~


# 参考资料

- 1. http://wklken.me/posts/2013/08/31/python-extra-coding-intro.html
- 2. https://github.com/urmyfaith/roadofios/blob/master/QuestionAndAnswer/xlsx2mdTable.py
- 3. https://github.com/urmyfaith/roadofios/blob/master/QuestionAndAnswer/xlsxCreateFile.py