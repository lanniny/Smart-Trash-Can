import serial
import time

# 配置串口
ser = serial.Serial(
    port='/dev/ttyS0',       # 您的设备名
    baudrate=115200,         # 波特率（与串口助手匹配）
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1                # 读取超时
)

if ser.is_open:
    print("串口已打开")
else:
    print("打开失败")
    exit(1)

try:
    # 循环发送测试（每秒发送一次，按 Ctrl+C 停止）
    while True:
        data_to_send = b"Hello, this is data from LubanCat 4 Python script!\n"
        ser.write(data_to_send)
        ser.flush()  # 立即刷新缓冲，确保数据发送
        print("已发送:", data_to_send.decode('utf-8').strip())
        time.sleep(1)  # 延时1秒
except KeyboardInterrupt:
    print("用户停止循环")
except Exception as e:
    print("错误:", e)
finally:
    ser.close()
    print("串口已关闭")
