from fastapi import FastAPI, HTTPException, status
from database import engine, inicializar_bd
from sqlmodel import Session
from models import Estudiante
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

inicializar_bd()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"Hello": "Hello World"}

# CRUD
# CREATE
# READ
# UPDATE Actualizar
# DELETE

@app.get("/estudiantes/{matricula}", response_model=Estudiante)
def leer_estudiante(matricula:str):
    with Session(engine) as session:
        estudiante = session.get(Estudiante, matricula)
        if not estudiante:
            raise HTTPException(status_code=404, detail="El estudiante no encontrado")
        return estudiante
    
@app.post("/estudiantes", response_model=Estudiante, 
          status_code=status.HTTP_201_CREATED)
def crear_estudiante(estudiante:Estudiante):
    with Session(engine) as session:
        session.add(estudiante)
        session.commit()
        session.refresh(estudiante)
        return estudiante
    
@app.delete("/estudiantes/{matricula}", 
            status_code=status.HTTP_204_NO_CONTENT)
def eliminar_estudiante(matricula:str):
    with Session(engine) as session:
        estudiante = session.get(Estudiante, matricula)
        if not estudiante:
            raise HTTPException(status_code=404, 
                                detail="El estudiante no encontrado")
        session.delete(estudiante)
        session.commit()

@app.put("/estudiantes/{matricula}", response_model=Estudiante)
def actualizar_estudiante(matricula:str, 
                          estudiante_actualizar:Estudiante):
    with Session(engine) as session:
        estudiante = session.get(Estudiante, matricula)
        if not estudiante:
            raise HTTPException(status_code=404, 
                                detail="El estudiante no encontrado")
        estudiante.nombre = estudiante_actualizar.nombre
        estudiante.apellidos = estudiante_actualizar.apellidos
        estudiante.genero = estudiante_actualizar.genero
        estudiante.direccion = estudiante_actualizar.direccion
        estudiante.telefono = estudiante_actualizar.telefono

        session.add(estudiante)
        session.commit()
        session.refresh(estudiante)
        return estudiante