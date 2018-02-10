```python
>>> data_list = [100, 200]
>>> data_list.extend(['暂无'] * (10 - len(data_list)))	#里面出现负数也没事
>>> data_list
[100, 200, '暂无', '暂无', '暂无', '暂无', '暂无', '暂无', '暂无', '暂无']

>>> key_list = ['num', 'city', 'qu']
>>> data_list = [100, 200]
>>> data = {each[0]: each[1] for each in zip(key_list, data_list)}
>>> data
{'num': 100, 'city': 200}

```

