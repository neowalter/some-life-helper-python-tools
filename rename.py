"""
Author: XI ZHOU
Time: 2021/6/13
Description: A simple tool to change the name of sepcific files. 

"""

import os


def rename_file(pathname=os.getcwd(), keyword, new_keyword=''):
    os.chdir(pathname)
    items = os.listdir(pathname)
    print('当前目录: ' + os.getcwd())
    for name in items :
        # 遍历所有文件
        if not os.path.isdir(name):
            if keyword in name :
                new_name = name.replace(keyword, new_keyword)
                os.rename(name,new_name)
        else:
            #递归所有子目录
            new_dir = os.path.join(pathname,name)
            print(new_dir)
            rename_file(new_dir, keyword, new_keyword)
            #返回上层目录
            os.chdir('..')      
    print('-----------------------分界线------------------------')
    print('当前目录: ' + os.getcwd())
    print('job finished')



keyword = input('type in the keywords that you want to delete:')
new_keyword = input('type in the keywords that you want to show:')
path = input('type in the directory that you want to modify:')
rename_file(path, keyword)
