# from operator import ge
# from turtle import shapesize
# from unittest import case
import xlwt
import os


xl = xlwt.Workbook(encoding='utf-8')

def getIterPath():
    fileroot = os.getcwd() + "\hn"
    filepath = os.listdir(fileroot)
    
    for files in filepath:
        files = fileroot + "\\" + files
        yield files

def getListFiles(pfile):
    return os.listdir(pfile)

def returnToXls(pfile,pout=".\\out"):
    xls = xlwt.Workbook(encoding='utf-8')
    files = os.listdir(pfile)
    pre_savename = "通话明细账单-仅通话用户数-"
    savename = pre_savename + pfile[-3:]+ ".xls"
    savedir = pout + "\\"
    # print(files,savename,type(files))
    if files:
        for file in files:
            sheet_name = file[-13:-4]
            sheet = xls.add_sheet(sheet_name,cell_overwrite_ok=False)
            filename = pfile + "\\" + file
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
            print(file,cal)
        xls.save(savedir+savename)
    else:
        sheet_name = pfile[-3:]
        sheet = xls.add_sheet(sheet_name,cell_overwrite_ok=False)
        sheet.write(0,0,"手机号")
        sheet.write(0,1,"通话时长")
        xls.save(savedir+savename)

if __name__ == "__main__":

    dfs = getIterPath()
    pout = ".\\output"
    for val in dfs:
        returnToXls(val,pout)

