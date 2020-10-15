# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:19:02 2020

@author: ntn080465
"""
import pyperclip
import pyautogui as pg
import os 
import glob
import shutil
import time

#os, glob を pathlib に置き換えたい

def EVA():

    
    def click_botton(filename, LR="left", clicks=1, pause=0.5):
        while True:
            try:
                x, y = pg.locateCenterOnScreen("fig/" + filename + ".PNG")
                break
            except TypeError:
                print("fig/" + filename + ".PNG がみつかりませんでした．")
                
        
        pg.click(
            x=x, 
            y=y, 
            pause=pause,
            clicks=clicks, 
            interval=0, 
            button=LR
        )
    
    
    #ファイル読み込み
    pg.click(834, 578)
    pg.press("alt")
    pg.press("enter")
    pg.press("down")
    pg.press("down")
    pg.press("enter")
    
    #ファイル全部選択
    pg.keyDown("shift")
    pg.keyDown("tab")
    pg.keyDown("tab")
    pg.keyUp("shift")
    pg.keyDown("ctrl")
    pg.keyDown("a")
    pg.keyUp("ctrl")
    
       
    #開く
    pg.keyDown("alt")
    pg.press("o")
    pg.keyUp("alt")
    time.sleep(5)
    
    click_botton("一覧", pause=1.0)
    
    click_botton("積分カーソル読み込み", pause=1.0)
           
    #積分カーソル選択
    pg.keyDown("shift")
    pg.press("tab")
    pg.keyUp("shift")
    pg.press("space")
    pg.press("enter")
    time.sleep(2)
    
    
    click_botton("積分", pause=5.0)
    click_botton("出力")
    pg.typewrite("temp")
    pg.click(470, 67)
    target = ("C:\\Users\\ntn080465\\Desktop\\EVA自動化\\Temp")
    pyperclip.copy(target)
    pg.keyDown("ctrl")
    pg.press("v")
    pg.keyUp("ctrl")
    time.sleep(0.3)
    pg.press("enter")
        
    #保存
    pg.keyDown("alt")
    pg.press("s")
    pg.keyUp("alt")
    
    time.sleep(1)
    
    #新規ファイル
    pg.keyDown("ctrl")
    pg.press("n")
    time.sleep(0.2)
    pg.keyUp("ctrl")
    pg.press("n")
    time.sleep(3)


    
if __name__=="__main__":
    
    """
    実行前にevaでtempdirからファイルを読み込んで，tempdirをデフォルトにする．
    """
    
    srcdir = "X:/XRDによる炭化物定量/10_標準資料作製/ブルカーXRD"
    tempdir = "Temp/"
    
    #Tempフォルダ内のファイル削除
    for file in os.listdir(tempdir):
            os.remove(os.path.join(tempdir,file))
    
    #srcdir内のサブフォルダを抽出
    dirs=[]
    for i in os.listdir(srcdir):  
        if os.path.isdir(os.path.join(srcdir, i)):
            dirs.append(i)

    #サブフォルダ内での処理．サブフォルダの中に測定1回分のデータが入っている．
    for directory in dirs:
        #実行中ディレクトリの表示
        print(directory)
        
        crtdir = os.path.join(srcdir, directory)
        
        #すでにrawファイルが存在する場合はスキップ．
        if glob.glob(os.path.join(crtdir, "*.raw"))!=[]:
            continue
        
        #サブフォルダ内のすべてのファイルをTempフォルダにコピー
        for file in os.listdir(crtdir):
            shutil.copyfile(os.path.join(crtdir, file), os.path.join(tempdir, file))
        
        EVA()
        
        #rawのファイル名．3文字目以降が数値なので，そこを取り出して2桁にしている．←非使用
        #filename = directory[3:].zfill(2)
        
        #ディレクトリ名をrawファイル名にする．
        filename = directory
        rawfile = glob.glob(os.path.join(tempdir + "/*.raw"))

        shutil.copyfile(rawfile[0], os.path.join(crtdir,filename + ".raw"))
        
        #Tempフォルダ内のファイル削除
        for file in os.listdir(tempdir):
            os.remove(os.path.join(tempdir,file))
    
    
    