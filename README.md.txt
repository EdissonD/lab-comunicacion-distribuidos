# Laboratorio — Comunicación entre Procesos y Sistemas Distribuidos

- Sockets TCP
- RPC (XML-RPC)
- API REST con FastAPI
- Diseño de arquitectura distribuida

---

# Parte 2 — Implementación Práctica

## Actividad 2.1 — Chat TCP
Chat bidireccional usando sockets TCP y threading.

Características:
- múltiples clientes,
- broadcast de mensajes,
- timestamps,
- desconexión segura.

---

## Actividad 2.2 — RPC
Sistema XML-RPC para cálculo de IMC.

Características:
- validación de errores,
- historial de cálculos,
- comunicación cliente-servidor.

---

## Actividad 2.3 — API REST
API CRUD de tareas usando FastAPI.

Endpoints:
- GET /tareas
- GET /tareas/{id}
- POST /tareas
- PUT /tareas/{id}
- DELETE /tareas/{id}

---

# Parte 3 — Arquitectura Distribuida
Diseño de plataforma EduConecta utilizando:
- WebSocket
- REST
- Kafka
- gRPC

---

# Tecnologías utilizadas
- Python
- FastAPI
- XML-RPC
- Sockets TCP
- Threading

---

# Ejecución

## Chat TCP

Servidor:
```bash
python servidor_chat.py