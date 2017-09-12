#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pickle 模块及其同类模块 cPickle 向 Python 提供了 pickle 支持。后者是用 C 编码的，它具有更好的性能
导入 cPickle ，并可以作为 pickle 来引用它
"""
import cPickle as pickle
t1 = ('this is a string', 42, [1, 2, 3], None)
print t1

"""
pickle 模块提供了以下函数对：
dumps(object) 返回一个字符串，它包含一个 pickle 格式的对象；loads(string) 返回包含在 pickle 字符串中的对象
dump(object, file) 将对象写到文件；load(file) 返回包含在 pickle 文件中的对象
"""
p1 = pickle.dumps(t1)
print p1
t2 = pickle.loads(p1)
print t2