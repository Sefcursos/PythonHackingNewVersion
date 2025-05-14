import socket

dominio = input("Introduce el dominio: ")
ip = socket.gethostbyname(dominio)
print(f"La IP de {dominio} es {ip}")