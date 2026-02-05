import socket

HOST = "0.0.0.0"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    
    while True:
        data = conn.recv(1024).decode("utf-8")
        if not data:
            break
        if data == "exit":
            break
        print(f"Received data: {data}")
        
        conn.sendall(data.encode("utf-8"))