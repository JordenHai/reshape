# from operator import ge
# from turtle import shapesize
# from unittest import case
from re import sub
import re
import xlwt
import os


xl = xlwt.Workbook(encoding='utf-8')

def getIterPath(resPath = '\\test'):
    fileroot = os.getcwd() + resPath
    filepath = os.listdir(fileroot)
    
    for files in filepath:
        files = fileroot + "\\" + files
        yield files

def getListFiles(pfile):
    return os.listdir(pfile)

def remakeFilename(pfile):
    subdirectory = os.listdir(pfile)
    pre_savename = "通话明细账单-仅通话用户数-"
    strs = pfile
    pname = strs.split("\\")[-1][:3]
    if subdirectory:
        pre_filename = subdirectory[0][-13:-9]
        end_filename = subdirectory[0][-13:-9]
        for file in subdirectory:
            pre_filename = file[-13:-9] if int(file[-13:-9]) <= int(pre_filename) else pre_filename
            end_filename = file[-13:-9] if int(file[-13:-9]) > int(end_filename) else end_filename
        savename = pre_savename + pname +'-' + pre_filename + '-' + end_filename + ".xls"
    else:
        savename = pre_filename + pname + ".xls"
    return savename

def ignoreExFilename(filename,pout=".\\output"):
    subFiles = getListFiles(pout)
    try:
        subFiles.index(filename)   
        flag = False 
    except:
        flag = True
    return flag

def returnToXls(pfile,pout=".\\out"):
    xls = xlwt.Workbook(encoding='utf-8')
    files = os.listdir(pfile)
    pre_savename = "通话明细账单-仅通话用户数-"
    # savename = pre_savename + pfile[-3:]+ ".xls"
    strs = pfile
    pname = strs.split("\\")[-1][:3]
    savedir = pout + "\\"
    if files:
        pre_filename = files[0][-13:-9]
        end_filename = files[0][-13:-9]
        for file in files:
            sheet_name = file[-13:-4]
            sheet = xls.add_sheet(sheet_name,cell_overwrite_ok=False)
            filename = pfile + "\\" + file
            pre_filename = file[-13:-9] if int(file[-13:-9]) <= int(pre_filename) else pre_filename
            end_filename = file[-13:-9] if int(file[-13:-9]) > int(end_filename) else end_filename
            print(filename)
            with open(filename,"r",encoding='utf-8') as fp:
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
        savename = pre_savename + pname +'-' + pre_filename + '-' + end_filename + ".xls"
        print(pre_filename,end_filename)
        xls.save(savedir+savename)
    else:
        sheet_name = pfile[-3:]
        sheet = xls.add_sheet(sheet_name,cell_overwrite_ok=False)
        sheet.write(0,0,"手机号")
        sheet.write(0,1,"通话时长")
        savename = pre_filename + pname + ".xls"
        xls.save(savedir+savename)

if __name__ == "__main__":

    dfs = getIterPath(resPath='\\hn')
    pout = ".\\output"
    for val in dfs:
        print("-----------------")
        # returnToXls(val,pout)
