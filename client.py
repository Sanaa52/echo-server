import socket

HOST = "10.90.14.76"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    while True:
        message = input("Введите сообщение (exit для выхода): ")
        s.sendall(message.encode("utf-8"))
        
        if message == "exit":
            break

        data = s.recv(1024).decode("utf-8")
        print(f"Ответ сервера: {data}")
