# Python_learn

[**1 python中的深复制与浅复制**](http://python.jobbole.com/82294/)

**[2 列表去重复内容](#2 列表去重复内容)**

[**3 sort  sorted**](#3 sort  sorted)

[**4 python3 把\u开头的unicode转中文，把str形态的unicode转中文**](#4 python3 把\u开头的unicode转中文，把str形态的unicode转中文)

[**5 属性操作**](#5 属性操作)

**2 列表去重复内容**

- list(set(list1))
- [list2.append(i) for i in list1 if i not in list2]
- [list2.sppend(i) for i in sorted(list1) if i not in list2]

**3 sort  sorted**

- sort函数只定义在list中，sorted函数对于所有的可迭代序列可以定义。

- sort函数对list直接修改，sorted返回修改后的序列。

  ```python
  >>> a = [5,7,6,3,4,1,2]
  >>> a.sort()
  >>> a
  [1, 2, 3, 4, 5, 6, 7]

  >>> student_tuples = [
          ('john', 'A', 15),
          ('jane', 'B', 12),
          ('dave', 'B', 10),
  ]
  >>> sorted(student_tuples, key=lambda student: student[2])   # 对学生通过年龄进行排序
  [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

  # 对类也适用
  >>> class Student:
          def __init__(self, name, grade, age):
                  self.name = name
                  self.grade = grade
                  self.age = age
          def __repr__(self):
                  return repr((self.name, self.grade, self.age))
  >>> student_objects = [
          Student('john', 'A', 15),
          Student('jane', 'B', 12),
          Student('dave', 'B', 10),
  ]
  >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
  [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

  # 忽略大小写排序
  >>> sorted("This is a test string from Andrew".split(), key=str.lower)
  ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
  ```

**4 python3 把\u开头的unicode转中文，把str形态的unicode转中文**

python3以上取消了decode，str.decode(“utf-8”)的话会报str没有decode方法的错 

```python
>>> print (a[0].encode('utf-8').decode('unicode_escape'))
生化危机
>>>
```
**5 属性操作**

- hasattr	getattr	delattr

  ```python
  delattr
  delattr(x, 'foobar') 相等于 del x.foobar

  hasattr
  #asattr(object, name)
  #判断一个对象里面是否有name属性或者name方法，返回BOOL值，有name特性返回True， 否则返回False。需要注意的是name要用括号括起来

  getattr
  #getattr(object, name[,default])
  #获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，可以在后面添加一对括号。
  >>> getattr(t, "age","18")  #若属性不存在，返回一个默认值。
  >>> '18'

  setattr
  #setattr(object, name, values)
  #给对象的属性赋值，若属性不存在，先创建再赋值。
  ```

  ​