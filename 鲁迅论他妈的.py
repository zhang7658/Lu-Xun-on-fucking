import time
import sys
print("本程序由JILILI_Jilili工作室编写，版权所有!")
print("注意：y表示同意，n表示拒绝。")
print("警告：本程序适合高配置计算机运行！")
def confirm():
    while True:
        response = input("确定要运行吗？(y/n): ")
        if response.lower() == 'y':
            return True
        elif response.lower() == 'n':
            sys.exit()
        else:
            print("请回答 y 或 n。")

if confirm():
    # 下面的代码会在用户输入 y 或 Y 后执行
    print("即将开始")
    # 在这里写下你想要执行的代码
print("鲁迅论他妈的，5秒钟后开始")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("0")
print("开始")
time.sleep(1)
for i in range(999999):
    print("他妈的",i)

