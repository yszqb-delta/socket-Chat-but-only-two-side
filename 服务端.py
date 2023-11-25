import socket

while True:
    door = int(input("请输入端口以建立连接(0~65535):"))
    if (door >= 0) and (door <= 65535):
        break
print("服务已启动")
print("本服务器IP:", socket.gethostbyname(socket.gethostname()), "端口:", door)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 调用socket中的socket()来创建一个socket s
    # 当代码离开with的时候，自动调用s.close()来销毁这个socket
    # AF_inet是IPv4
    # SOCK_STREAM是TCP
    s.bind(("0.0.0.0", door))
    # 0.0.0.0表示电脑任意网卡可使用这个socket
    # 1234是端口
    s.listen()
    # 设为监听状态
    c, addr = s.accept()
    # accept表示接受任意客户端的连接 并返回一个新的socket c以及对应IP
    # socket s主要用于监听，socket c主要用于通信
    with c:
        print(addr, "连接")
        while True:
            data = c.recv(1024)
            # 接收消息
            if not data:
                break
                # 数据不为空
            else:
                print(data.decode())
            data2 = b''
            data2 += input("请输入:").encode()
            c.sendall(data2)
