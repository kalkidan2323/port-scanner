# simple port scanner scan range of ports(1-100)
import socket


target = input("Enter target IP: ")
port = int(input("Enter port number: "))

try:
    s = socket.socket()
    s.settimeout(2)
    s.connect((target, port))
    print(f"Port {port} is OPEN")
except:
    print(f"Port {port} is CLOSED")
   # multiport scanner
import socket

target = input("Enter target IP: ")
print("Scanning...")

for port in range(1, 101):
    s = socket.socket()
    s.settimeout(0.5)
    try:
        s.connect((target, port))
        print(f"Port {port} OPEN")
        s.close()
    except:
        pass
   # fast port scannerimport socket

target = input("Enter target IP: ")
print("Scanning...")

for port in range(1, 101):
    s = socket.socket()
    s.settimeout(0.5)
    try:
        s.connect((target, port))
        print(f"Port {port} OPEN")
        s.close()
    except:
        pass
