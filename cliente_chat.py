import socket
import threading

HOST = '127.0.0.1'
PORT = 5000


def recibir_mensajes(cliente):
    """
    Recibe mensajes del servidor
    continuamente.
    """
    while True:
        try:
            mensaje = cliente.recv(1024).decode()

            if not mensaje:
                break

            print("\n" + mensaje)

        except:
            break


def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    cliente.connect((HOST, PORT))

    # Hilo para recibir mensajes
    hilo_recibir = threading.Thread(
        target=recibir_mensajes,
        args=(cliente,)
    )

    hilo_recibir.daemon = True
    hilo_recibir.start()

    print("Conectado al chat.")
    print("Escribe SALIR para desconectarte.\n")

    while True:
        mensaje = input()

        cliente.sendall(mensaje.encode())

        if mensaje.upper() == "SALIR":
            break

    cliente.close()


if __name__ == "__main__":
    iniciar_cliente()