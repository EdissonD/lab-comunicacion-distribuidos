import socket
import threading
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5000

# LISTA GENERAL DE LOS CLIENTES CONECTADOS
clientes = []

# lock para evitar problemas de concurrencia
lock = threading.Lock()

def broadcast(mensaje, cliente_emisor):
    """
    Envia el mensaje a todos los clientes 
    excepto al que lo envio
    """
    with lock:
        for cliente in clientes:
            if cliente != cliente_emisor:
                try:
                    cliente.sendall(mensaje.encode())
                except:
                    clientes.remove(cliente)
def manejar_cliente(conn, addr):
    """
    Maneja la comunicación individual
    con un cliente.
    """

    print(f"[NUEVA CONEXIÓN] {addr[0]}:{addr[1]} conectado.")

    while True:
        try:
            data = conn.recv(1024)

            if not data:
                break

            mensaje = data.decode().strip()

            # Timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Registro en consola
            print(f"[{timestamp}] {addr[0]}:{addr[1]} → '{mensaje}'")

            # Cliente quiere salir
            if mensaje.upper() == "SALIR":
                conn.sendall("Desconectado del servidor.".encode())
                break

            mensaje_broadcast = f"{addr[0]}:{addr[1]} dice: {mensaje}"

            # Enviar a los demás clientes
            broadcast(mensaje_broadcast, conn)

        except:
            break

    # Eliminar cliente de la lista
    with lock:
        if conn in clientes:
            clientes.remove(conn)

    conn.close()

    print(f"[DESCONECTADO] {addr[0]}:{addr[1]}")


def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"[SERVIDOR INICIADO] Escuchando en {HOST}:{PORT}")

    while True:
        conn, addr = servidor.accept()

        with lock:
            clientes.append(conn)

        hilo = threading.Thread(
            target=manejar_cliente,
            args=(conn, addr)
        )

        hilo.start()


if __name__ == "__main__":
    iniciar_servidor()