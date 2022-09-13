import xlwt
import os

filepath = os.getcwd() + "\hn"
files = os.listdir(filepath)

xl = xlwt.Workbook(encoding='utf-8')

for file in files:
    sheet_name = file[-13:-4]
    sheet = xl.add_sheet(sheet_name,cell_overwrite_ok=False)
    filename = filepath + "\\" + file
    with open(filename,"r") as fp:
        vals = fp.readlines()
    index = 1
    cal = 0
    col = [0,1]
    sheet.write(0,0,"手机号")
    sheet.write(0,1,"通话时长")
    for val in vals:
        res = val.split(",")
        if int(res[1]) == 0:
            pass
        else:
            sheet.write(index,col[0],res[0])
            sheet.write(index,col[1],res[1])
            index = index + 1
            cal = cal + 1
            if index == 65535:
                index = 1
                col[0] = col[0] + 2
                col[1] = col[1] + 2
                sheet.write(0,col[0],"手机号")
                sheet.write(0,col[1],"通话时长") 
    print(len(vals))
xl.save("通话明细账单-仅通话用户数修正版0810-0815.xls")