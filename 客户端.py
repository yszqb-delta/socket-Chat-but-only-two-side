import socket

ip = input("请输入服务器ip:")
while True:
    door = int(input("请输入端口以建立连接(0~65535):"))
    if door >= 0 or door <= 65535:
        break
print("服务已启用")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip, door))
    while True:
        data = b''
        data += input("请输入:").encode()
        s.sendall(data)
        data = s.recv(1024)
        print("回答:", data.decode())
