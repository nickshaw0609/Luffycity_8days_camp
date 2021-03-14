"""
1. 准备一台安卓手机 & 电脑安装模拟器
2. 网上下载安卓工具adb（安卓官方）
3. 用代码去下发命令
    代码 -> adb -> 手机（模拟器）
"""


import time
import subprocess

adb_path = r"E:\Luffy_Camp_8days\auto_TikTok_tool\tools\platform-tools-win\adb.exe"

# 1. 关闭和启动adb服务
subprocess.run(f"{adb_path}  kill-server")
subprocess.run(f"{adb_path}  start-server")
subprocess.run(f"{adb_path}  connect 127.0.0.1:7555")  # mumu模拟器win系统接口

# 2.监测连接的设备列表
res = subprocess.run(f"{adb_path} devices")
print(res)
"""
PKT0220320004379	device
emulator-5554	device
"""


# 3.指定设备，并发发送指令（点击）
# subprocess.getoutput(f"{adb_path} -s emulator-5554 shell input tap 324 456")


# 4.指定设备，并发发送指令（滑动）
# subprocess.getoutput(f"{adb_path} -s emulator-5554 shell input swipe 311 952 622 444 400")

# 5.指定设备，并发发送指令循环执行。
while True:
    # subprocess.run(f"{adb_path} -s 285ada6c04047ece shell input swipe 1155 1786 418 1786 400")  # 手机自动向左滑屏
    # subprocess.run(f"{adb_path} -s 127.0.0.1:7555 shell input swipe 427 976 427 589 400")  # 自动刷抖音
    subprocess.run(f"{adb_path} -s 285ada6c04047ece shell input tap 2538 1286")  # 明日方舟自动刷关卡
    time.sleep(1)  # 停顿4s

# 6.其他更多指令
"""
其他更多指令：
    - 查看手机设备：adb devices
    - 查看设备型号：adb shell getprop ro.product.model
    - 查看电池信息：adb shell dumpsys battery
    - 查看设备ID：adb shell settings get secure android_id
    - 查看设备IMEI：adb shell dumpsys iphonesubinfo
    - 查看Android版本：adb shell getprop ro.build.version.release
    - 查看手机网络信息：adb shell ifconfig
    - 查看设备日志：adb logcat
    - 重启手机设备：adb reboot
    - 安装一个apk：adb install /path/demo.apk
    - 卸载一个apk：adb uninstall <package>
    - 查看系统运行进程：adb shell ps
    - 查看系统磁盘情况：adb shell ls /path/
    - 手机设备截屏：adb shell screencap -p /sdcard/aa.png
    - 手机文件下载到电脑：adb pull /sdcard/aa.png ./
    - 电脑文件上传到手机：adb push aa.png /data/local/
    - 手机设备录像：adb shell screenrecord /sdcard/ab.mp4
    - 手机屏幕分辨率：adb shell wm size
    - 手机屏幕密度：adb shell wm density
    - 手机屏幕点击：adb shell input tap xvalue yvalue
    - 手机屏幕滑动：adb shell input swipe 1000 1500 200 200
    - 手机屏幕带时间滑动：adb shell input swipe 1000 1500 0 0 1000
    - 手机文本输入：adb shell input text xxxxx
    - 手机键盘事件：adb shell input keyevent xx
"""
