import random
from instagrapi import Client
from getpass import getpass
from colorama import Fore, init
from pyfiglet import Figlet
import keyboard
import time  # Importa el módulo time
import os
import sys

init()
f = Figlet(font='slant')
print(Fore.GREEN + f.renderText('InstaLiker')+ "                        By Aforak y EsponjiMan")
print("####################################################")
usuario = input(Fore.WHITE + 'Introduce usuario: ')
password = getpass('Introduce clave: ')

#COMIENZA LA CONEXIÓN
client=Client()
client.login(f"{usuario}",f"{password}")
print(Fore.GREEN + "[*]" + Fore.WHITE + "¡Conectado!")
#CONEXIÓN REALIZADA

#MENÚ
def menu():
    # Limpiar el buffer de entrada
    if os.name == 'nt':
        os.system('cls')
    else:
        sys.stdin.flush()
    print(Fore.WHITE + "############# MENÚ ############")
    print(Fore.WHITE + "Abrir menú - Pulsa " + Fore.GREEN + "M" )
    print(Fore.WHITE + "Dar likes automáticamente por tema - Pulsa " + Fore.GREEN + "L" )
    print(Fore.WHITE + "Seguir usuario - Pulsa " + Fore.GREEN + "W" )
    print(Fore.WHITE + "Enviar MD - " + Fore.RED + "EN DESARROLLO" )
    print(Fore.WHITE + "Salir del menú - Pulsa " + Fore.RED + "CNTRL + C" )
    print(Fore.WHITE + "###############################")

keyboard.add_hotkey("m", menu)  # Asignación de la tecla a la función

def dar_likes():
    # Limpiar el buffer de entrada
    if os.name == 'nt':
        os.system('cls')
    else:
        sys.stdin.flush()
    print(Fore.GREEN + "INFO: " + Fore.WHITE + "¡Has elegido la opción de Dar Likes por temas!")
    cantidad=int(input(Fore.YELLOW + "Borra las letras que salen apartir de los dos puntos" + Fore.WHITE + " e introduce la cantidad de likes que quieres dar: "))
    hastag=input('Elige sobre que tema serán las publicaciones,' + Fore.YELLOW + " no uses hashtag: " + Fore.WHITE + "")
    medias= client.hashtag_medias_recent(hastag,cantidad)
    for i,media in enumerate(medias):
        client.media_like(media.id)
        print(Fore.GREEN + "[*]" + Fore.WHITE + f"¡Has dado like a  {i+1} publicaciones sobre #{hastag}!")
    print("¡Acciones realizadas con éxito!")
    print(Fore.GREEN + "INFO: " + Fore.WHITE + "Pulsa 'M' para abrir el menú")
keyboard.add_hotkey("l", dar_likes)  # Asignación de la tecla a la función

def enviar_mensaje():
    # Limpiar el buffer de entrada
    if os.name == 'nt':
        os.system('cls')
    else:
        sys.stdin.flush()
    print(Fore.GREEN + "INFO: " + Fore.WHITE + "¡Has elegido la opción de enviar un mensaje directo!")
    usuario_destino = input(Fore.YELLOW + "Introduce el nombre de usuario al que quieres enviar el mensaje: " + Fore.WHITE)
    mensaje = input(Fore.YELLOW + "Introduce el mensaje que quieres enviar: " + Fore.WHITE)
    user_id = client.user_id_from_username(usuario_destino)
    client.direct_send(mensaje, user_id)
    print(Fore.GREEN + "[*]" + Fore.WHITE + f"¡Has enviado un mensaje a {usuario_destino}!")

def seguir_usuarios():
    import instagrapi.exceptions
    # Limpiar el buffer de entrada
    if os.name == 'nt':
        os.system('cls')
    else:
        sys.stdin.flush()
    print(Fore.GREEN + "INFO: " + Fore.WHITE + "¡Has elegido la opción de seguir a los usuarios!")
    cantidad=int(input(Fore.YELLOW + "Borra las letras que salen apartir de los dos puntos" + Fore.WHITE + " e introduce la cantidad de usuarios que quieres seguir: "))
    hastag=input('Elige sobre que tema serán las publicaciones,' + Fore.YELLOW + " no uses hashtag: " + Fore.WHITE + "")
    medias= client.hashtag_medias_recent(hastag,cantidad)
    for i,media in enumerate(medias):
        try:
            client.user_follow(media.user.pk)  # Cambio aquí
            print(Fore.GREEN + "[*]" + Fore.WHITE + f"¡Has seguido al usuario de la publicación {i+1} sobre #{hastag}!")
        except instagrapi.exceptions.FeedbackRequired:
            print(Fore.RED + "[!]" + Fore.WHITE + f"No se pudo seguir al usuario de la publicación {i+1} sobre #{hastag} debido a sus configuraciones de privacidad.")
    print("¡Acciones realizadas con éxito!")
    print(Fore.GREEN + "INFO: " + Fore.WHITE + "Pulsa 'M' para abrir el menú")

keyboard.add_hotkey("w", seguir_usuarios)  # Asignación de la tecla a la función






while True:  # Bucle infinito
    print(Fore.GREEN + "INFO: " + Fore.WHITE + "Pulsa 'M' para abrir el menú")
    time.sleep(210)  # Pausa de 1 segundo
    if keyboard.is_pressed('q'):  # Si el usuario presiona 'q', se rompe el bucle
        break



