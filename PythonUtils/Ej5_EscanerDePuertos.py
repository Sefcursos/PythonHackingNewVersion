## SCRIPT DE USO EDUCATIVO ##
# DESARROLLO DE UN ESCÁNER DE PUERTOS CON INTERFAZ GRÁFICA Y ESCANEO MULTIHILO PARA CURSO DE HACKING ÉTICO. TODA ESTA INFORMACIÓN ES DE MANERA EDUCATIVA.

import socket # Permite crear conexiones de red y escanear puertos.
import platform # Detecta el sistema operativo (Windows, Linux...).
import subprocess # Ejecuta comandos del sistema para obtener la IP local.
import time # Usado para pausas y barra de progreso
import threading
import tkinter as tk
from tkinter import ttk, messagebox
import queue
import re
import locale


# Diccionario con puertos comunes asociados a vulnerabilidades o malas prácticas de seguridad
puertos_vulnerables = {
    21: "FTP (sin cifrado, susceptible a sniffing y brute force)",
    23: "Telnet (inseguro, sin cifrado)",
    25: "SMTP (posible open relay)",
    110: "POP3 (sin cifrado)",
    139: "NetBIOS (puede exponer archivos en red)",
    143: "IMAP (sin cifrado)",
    445: "SMB (explotable por EternalBlue)",
    3306: "MySQL (brute force, acceso remoto)",
    3389: "RDP (ataques RCE, brute force)",
    5900: "VNC (sin autenticación en muchos casos)",
    8080: "HTTP Alternativo (admin panels expuestos)"
}
# Función que detecta la IP local del equipo para escanearla.
def obtener_ip_local():
    sistema = platform.system() # Detecta si estás en windows, linux, etc.
    if sistema == "Windows":
        resultado = subprocess.check_output("ipconfig", encoding='850')
        for linea in resultado.splitlines():
            if "IPv4" in linea:
                return  linea.split(":")[-1].strip()
    else:
        resultado = subprocess.check_output("hostname -I", shell=True)
        return resultado.decode().split()[0]

def validar_ip(ip):
    patron = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if patron.match(ip):
        partes = ip.split(".")
        return all(0 <=)


# Función imprime una barra de progreso tipo [####------] 40%
# def mostrar_barra(progreso, total, largo=30):
#     porcentaje = progreso / total
#     completado = int(porcentaje * largo)
#     barra = "#" * completado + "-" * (largo - completado)
#     print(f"\r[ {barra} ] {porcentaje *100:.1f}% ", end="")

# Función encargada de ejecutar el escaneo de puertos
def escaner_de_puertos(ip, rango=(1, 100)):
    total_puertos = rango[1] - rango[0] + 1
    puertos_abiertos = []

    print(f"\n[+] Escaneando puertos en {ip}....\n")

    for port, puerto in enumerate(range(rango[1] - rango[0] + 1), start=1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.socket(): te crea un nuevo objeto de socket, socke.AF_INET: Indica que se esta utilizando la familia de direcciones IPv4 (192.168.0.1), socket.SOCK_STREAM: Esto especifica que el socket sera de tipo STREAMM,osea que utilizara el protocolo tCP (Transmission Control Protocol), el cual proporciona una conexión confiable.
        sock.settimeout(0.3)
        resultado = sock.connect_ex((ip, puerto))
        if resultado == 0:
            puertos_abiertos.append(puerto)
        sock.close()

        mostrar_barra(port, total_puertos)
        time.sleep(0.01)

    print("\n\n[+] Puertos abiertos encontrados:")
    if puertos_abiertos:
        for p in puertos_abiertos:
            advertencia = ""
            if p in puertos_vulnerables:
                advertencia = f" VULNERABLE --> {puertos_vulnerables}"
            print(f"     - Puerto {p} abierto {advertencia}")
    else:
        print("  - Ninguno en el rango especificado.")



# Ejecutar escaneo (Lamamos a la función)
ip_objetivo = obtener_ip_local()
escaner_de_puertos(ip_objetivo)



