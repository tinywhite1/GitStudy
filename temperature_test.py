import serial
import time
# write a function add two elemen
def add(a,b):
    return a+b
# 写一个温度传感器串口通信的测试程序
#




# 建立与串口的连接，注意根据设备管理器调整串口
ser = serial.Serial('COM3', 9600, timeout=0.1)

previous_temperature = None  # 定义一个全局变量来存储上次的温度
# 发送指令到传感器的函数
def send_command(command):
    ser.write(bytearray(command))

# 读取温度传感器串口发送来的数据
def read_temperature():
    global previous_temperature  # 使用全局变量
    if ser.in_waiting > 0:
        data = ser.read(9)  # 尝试读取9个字节，对应一包数据
        if len(data) == 9 and data[0] == 0xFE:
            mode = data[1]
            temp_h = data[2]
            temp_l = data[3]
            checksum = sum(data[:-1]) & 0xFF  # 计算校验和并只保留低8位
            if checksum == data[-1]:  # 检查校验和是否正确
                temperature = temp_h + temp_l / 100.0
                # 如果当前读取的温度大于90°C，打印上次的温度（如果有）
                if temperature > 90 and previous_temperature is not None:
                    if mode == 0xAA:  # 物温模式
                        print(f"Object Temperature: {previous_temperature} °C")
                    elif mode == 0xAC:  # 体温模式
                        print(f"Body Temperature: {previous_temperature} °C")
                else:
                    previous_temperature = temperature  # 更新存储的温度为当前读取值
                    if mode == 0xAA:  # 物温模式
                        print(f"Object Temperature: {temperature} °C")
                    elif mode == 0xAC:  # 体温模式
                        print(f"Body Temperature: {temperature} °C")

# 主循环
try:
    while True:
        # 设置物温模式
        #send_command([0xFA, 0xC6, 0xC0])
        
        # 设置体温模式
        send_command([0xFA, 0xC5, 0xBF])
        
        # 开始测温并上传温度
        send_command([0xFA, 0xCA, 0xC4])

        # 等待片刻，确保数据能够从传感器发送至串口
        time.sleep(0.2)
        
        # 尝试读取并打印温度
        read_temperature()

        # 稍作延迟，避免过快地发送指令
        time.sleep(0.2)

except KeyboardInterrupt:
    # 按下 Ctrl+C 结束程序
    print("Program stopped by user.")
finally:
    ser.close()  # 确保程序结束时关闭串口连接
