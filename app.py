from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

# =========================
# MODELO DE DATOS
# =========================

class Tarea(BaseModel):
    titulo: str
    descripcion: str


# =========================
# BASE DE DATOS EN MEMORIA
# =========================

tareas: Dict[int, dict] = {}

contador_id = 1


# =========================
# GET /tareas
# Retorna todas las tareas
# =========================

@app.get("/tareas")
def obtener_tareas():
    return list(tareas.values())


# =========================
# GET /tareas/{id}
# Retorna una tarea por ID
# =========================

@app.get("/tareas/{id}")
def obtener_tarea(id: int):

    if id not in tareas:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    return tareas[id]


# =========================
# POST /tareas
# Crear una o varias tareas
# =========================

@app.post("/tareas")
def crear_tarea(lista_tareas: List[Tarea]):

    global contador_id

    creadas = []

    for tarea in lista_tareas:
        nueva_tarea = {
            "id": contador_id,
            "titulo": tarea.titulo,
            "descripcion": tarea.descripcion,
            "completada": False
        }
        tareas[contador_id] = nueva_tarea
        contador_id += 1
        creadas.append(nueva_tarea)

    return {
        "mensaje": f"{len(creadas)} tarea(s) creada(s) correctamente",
        "tareas": creadas
    }


# =========================
# PUT /tareas/{id}
# Completar tarea
# =========================

@app.put("/tareas/{id}")
def completar_tarea(id: int):

    if id not in tareas:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    tareas[id]["completada"] = True

    return {
        "mensaje": "Tarea completada",
        "tarea": tareas[id]
    }


# =========================
# DELETE /tareas/{id}
# Eliminar tarea
# =========================

@app.delete("/tareas/{id}")
def eliminar_tarea(id: int):

    if id not in tareas:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    tarea_eliminada = tareas.pop(id)

    return {
        "mensaje": "Tarea eliminada",
        "tarea": tarea_eliminada
    }