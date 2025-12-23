user loging 

from datetime import datetime

file = open("input_log.txt", "a")

while True:
    cmd = input("Enter command: ")
    if cmd == "exit":
        break
    file.write(f"{datetime.now()} - {cmd}\n")

file.close()
