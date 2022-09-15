# from operator import ge
# from turtle import shapesize
# from unittest import case
import re
from sys import flags
import xlwt
import os


xl = xlwt.Workbook(encoding='utf-8')

def getIterPath(resPath = '\\test'):
    # 原始数据目录
    fileroot = os.getcwd() + resPath
    # 遍历原始目录,得到子目录列表
    subdirectory = os.listdir(fileroot)
    # 遍历子目录列表，制作生成器，获取完整子目录路径
    for subdirectoryname in subdirectory:
        subdirectorypath = fileroot + "\\" + subdirectoryname
        # 生成器
        yield subdirectorypath

def getListFiles(subdirectorypath):
    return os.listdir(subdirectorypath)

def remakeFilename(subdirectorypath):
    subdirectory = os.listdir(subdirectorypath)
    pre_savename = "通话明细账单-仅通话用户数-"
    subdirectorypaths = subdirectorypath
    pname = subdirectorypaths.split("\\")[-1][:3]
    if subdirectory:
        pre_filename = subdirectory[0][-13:-9]
        end_filename = subdirectory[0][-13:-9]
        for file in subdirectory:
            pre_filename = file[-13:-9] if int(file[-13:-9]) <= int(pre_filename) else pre_filename
            end_filename = file[-13:-9] if int(file[-13:-9]) > int(end_filename) else end_filename
        savename = pre_savename + pname +'-' + pre_filename + '-' + end_filename + ".xls"
    else:
        savename = pre_savename + pname + ".xls"
    return savename

def ignoreExFilename(filename,pout=".\\output"):
    subFiles = getListFiles(pout)
    try:
        subFiles.index(filename)  
        flag = False  
    except:
        flag = True
    return flag

def returnToXls(subdirectorypath,pout=".\\out"):
    xls = xlwt.Workbook(encoding='utf-8')
    subdirectory = os.listdir(subdirectorypath)
    # print(subdirectory,subdirectorypath)
    savename = remakeFilename(subdirectorypath)
    flag = ignoreExFilename(filename=savename)
    savedir = pout + "\\" 
    if flag:
        if subdirectory:
            for file in subdirectory:
                sheet_name = file[-13:-4]
                sheet = xls.add_sheet(sheet_name,cell_overwrite_ok=False)
                filename = subdirectorypath + "\\" + file
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
            xls.save(savedir+savename)
        else:
            sheet_name = subdirectorypath[-3:]
            sheet = xls.add_sheet(sheet_name,cell_overwrite_ok=False)
            sheet.write(0,0,"手机号")
            sheet.write(0,1,"通话时长")
            xls.save(savedir+savename)

if __name__ == "__main__":

    dfs = getIterPath(resPath='\\hn')
    pout = ".\\output"
    for subdirectorypath in dfs:
        returnToXls(subdirectorypath,pout)
    print("end~")