# Python_learn

[python中的深复制与浅复制](http://python.jobbole.com/82294/)

列表去重复内容

- list(set(list1))
- [list2.append(i) for i in list1 if i not in list2]
- [list2.sppend(i) for i in sorted(list1) if i not in list2]