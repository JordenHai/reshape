import re
import shelve
import pandas as pd
import os

relativePath = os.getcwd()[:-4]
excelPath = relativePath + '/' + 'test' 

excelfiles = os.listdir(excelPath)
res = excelPath + "/" + excelfiles[0]
# 不知道sheetname
df = pd.read_excel(res,sheet_name=None)
# 这种是返回的 dict_keys 需要转换成list
sheets = list(df.keys())
# 获知sheetname方式
df = pd.read_excel(res,sheet_name=sheets[0])
datakeys = df.keys()

print(datakeys)

datevalues = df.values

print(datevalues)

val = datevalues[0]
print(val)

# for vals in datevalues:
#     for index in range(len(datakeys)):
#         print(vals[index])

# loc[]          按照索引值定位
# iloc[]         按照索引位置定位
# ix=            均可
# axis=          0 纵 1 横 单位是行
# df.head(2)     读取前两行的数据，dataFrame结构
# df.iloc[:2]    == head

# df.tail(2)     读取后两行的数据，dataFrame结构

