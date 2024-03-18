#定义需要安装的包
#编译器需要的包
program_packages=['gcc','g++','cmake','ccache','python3-pip','python3-venv']
#终端环境需要的包
console_packages=['fish','vim','neofetch','git','btop','nala']
#qt环境需要的包
qt_packages=['qt5-default', 'qt5-qmake', 'qtcreator']



import subprocess

#镜像源更新函数
def update():
    # 执行 apt update
    update_process = subprocess.Popen(['apt', 'update'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    update_output, update_error = update_process.communicate()

    print('UPDATE RESULT:')
    print('-'*20)
    print(update_output.decode('utf-8'))
    print('*'*20)
    print('UPDATE ERROR:')
    print('-'*20)
    print(update_error.decode('utf-8'))


#系统更新函数
def upgrade():
    # 执行 apt upgrade
    upgrade_process = subprocess.Popen(['apt', 'upgrade','-y'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    upgrade_output, upgrade_error = upgrade_process.communicate()

    print('UPGRADE RESULT:')
    print('-'*20)
    print(upgrade_output.decode('utf-8'))
    print('*'*20)
    print('UPGRADE ERROR:')
    print('-'*20)
    print(upgrade_error.decode('utf-8'))

import apt

#包检查函数
def check()->set:
    all_packages=program_packages
    all_packages.extend(console_packages)
    all_packages.extend(qt_packages)
    #查询系统已安装的包
    cache=apt.Cache()
    #定义已安装，未安装，不存在的set
    installed=set()
    non_installed=set()
    non_existed=set()
    
    #遍历需要安装的包
    for package_name in all_packages:
        #先检查是否存在
        if package_name in cache:
            #存在的话查看是否安装
            package=cache[package_name]
            if package.installed:
                installed.add(package_name)
            else:
                non_installed.add(package_name)
        else:
            non_existed.add(package_name)
    
    #输出结果
    print('$'*20)
    print('Packages has installed:')
    print(installed)
    print(r"Packages ditn't existed:")
    print(non_existed)
    print("Packages needed to installed:")
    print(non_installed)
    print('$'*20)
    return non_installed

#包安装函数
def install():
    packages=check()
    cache=apt.Cache()
    length=len(packages)
    print(f"{length} packages needed to install...")
    for i,p in enumerate(packages):
        print(f"{i+1}/{length}:{p} is installing")
        package=cache[p]
        package.mark_install()
        cache.commit()
        print(f"{i+1}/{length}:{p} installed sucessfully")
    print("All packages has installed, have a nice day!")


import argparse

parser=argparse.ArgumentParser()
#添加是否更新源的参数
parser.add_argument('-up','--update',action='store_true',help='Refresh apt mirror list')
#添加是否更新系统的参数
parser.add_argument('-ug','--upgrade',action='store_true',help='Upgrade system')
#添加是否检查包情况的参数
parser.add_argument('-c','--check',action='store_true',help='Check packages status')
#添加是否开始安装包的参数
parser.add_argument('-i','--install',action='store_true',help='Install all packages required')
#解析命令行参数
args=parser.parse_args()

if args.update:
    print('Starting to refresh mirror...')
    update()

if args.upgrade:
    print('Starting to upgrade system...')
    upgrade()

if args.check:
    check()

if args.install:
    install()