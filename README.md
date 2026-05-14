Comunicación entre Procesos y Sistemas Distribuidos

## Integrante
- Marcelo

---

# Descripción

Este laboratorio implementa diferentes mecanismos de comunicación entre procesos y sistemas distribuidos estudiados en clase:

- Sockets TCP
- RPC (XML-RPC)
- API REST con FastAPI
- Diseño de arquitectura distribuida

El objetivo fue comprender cuándo y cómo utilizar mecanismos síncronos y asíncronos en distintos escenarios reales.

---

# Parte 2 — Implementación Práctica

## Actividad 2.1 — Chat TCP

Implementación de un chat bidireccional usando sockets TCP y threading en Python.

### Características

- Soporte para múltiples clientes simultáneos
- Broadcast de mensajes
- Registro de mensajes con timestamps
- Desconexión segura mediante comando `SALIR`

### Archivos

- `servidor_chat.py`
- `cliente_chat.py`

---

## Actividad 2.2 — RPC (XML-RPC)

Sistema cliente-servidor usando XML-RPC para cálculo de IMC.

### Funcionalidades

- Cálculo de IMC
- Clasificación:
  - Bajo peso
  - Normal
  - Sobrepeso
  - Obesidad
- Validación de errores
- Historial de cálculos

### Archivos

- `servidor_rpc.py`
- `cliente_rpc.py`

---

## Actividad 2.3 — API REST con FastAPI

API REST para gestión de tareas (TODO list).

### Endpoints

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/tareas` | Obtener todas las tareas |
| GET | `/tareas/{id}` | Obtener tarea por ID |
| POST | `/tareas` | Crear tarea |
| PUT | `/tareas/{id}` | Completar tarea |
| DELETE | `/tareas/{id}` | Eliminar tarea |

### Características

- Datos almacenados en memoria
- Manejo de errores HTTP
- Respuestas JSON
- Documentación Swagger automática

### Archivo

- `app.py`

---

# Parte 3 — Diseño de Arquitectura

Diseño de la plataforma educativa distribuida **EduConecta**.

### Tecnologías seleccionadas

| Funcionalidad | Tecnología |
|---|---|
| Chat en vivo | WebSocket |
| Catálogo móvil | REST |
| Notificaciones | Kafka |
| Microservicios internos | gRPC |

### Objetivos del diseño

- Baja latencia
- Escalabilidad
- Desacoplamiento
- Comunicación eficiente

---

# Tecnologías Utilizadas

- Python
- FastAPI
- XML-RPC
- Sockets TCP
- Threading
- Uvicorn

---

# Ejecución de los programas

## Chat TCP

### Servidor

```bash
python servidor_chat.py
