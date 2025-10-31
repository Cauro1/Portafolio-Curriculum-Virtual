from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from pathlib import Path

app = FastAPI(
    title="Portafolio Jeremy Cauro",
    description="Portafolio personal desarrollado con FastAPI",
    version="1.0.0"
)

# Configuración de rutas multiplataforma
BASE_DIR = Path(__file__).parent

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Modelos de datos
class PersonalInfo(BaseModel):
    name: str
    title: str
    email: str
    phone: str
    location: str
    about: str

class Experience(BaseModel):
    id: int
    position: str
    period: str
    description: str

# Datos - Experiencia
personal_info = PersonalInfo(
    name="Jeremy Alejandro Cauro Peraza",
    title="Desarrollador de Páginas Web - Analista en Sistemas",
    email="cauroperazajeremyalejandro@gmail.com",
    phone="+58 412-9340714",
    location="Acarigua, Venezuela",
    about="Soy un estudiante del 4°to semestre actualmente de la IUTEPI; un apasionado desarrollador en crear soluciones usando Python, FastAPI y tecnologías modernas."
)

experience_db = [
    Experience(
        id=1,
        position="Desarrollador de Páginas Web",
        period="2025 - Presente",
        description="Desarrollo y mantenimiento de APIs RESTful con FastAPI, implementación de microservicios y optimización de bases de datos. Especializado en crear soluciones escalables y eficientes para aplicaciones web modernas.",
        technologies=["Python", "FastAPI", "PostgreSQL", "C++", "HTML5", "JavaScript"]
    )
]

# Rutas de la aplicación
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Página principal del portafolio"""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "personal_info": personal_info,
        "experiences": experience_db
    })

@app.get("/api/info")
async def get_personal_info():
    """API endpoint para obtener información personal"""
    return personal_info

@app.get("/api/experience")
async def get_experience_api():
    """API endpoint para obtener experiencia"""
    return experience_db

@app.post("/contact")
async def contact_form(
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...)
):
    """
    Endpoint para procesar el formulario de contacto.
    """
    print(f"\n{'='*50}")
    print("NUEVO MENSAJE DE CONTACTO RECIBIDO:")
    print(f"Nombre: {name}")
    print(f"Email: {email}")
    print(f"Asunto: {subject}")
    print(f"Mensaje: {message}")
    print(f"{'='*50}\n")
    
    return {
        "status": "success",
        "message": "¡Mensaje recibido correctamente! Te contactaré pronto."
    }

@app.get("/health")
async def health_check():
    """Endpoint para verificar el estado del servidor"""
    return {
        "status": "healthy", 
        "service": "portfolio-api",
        "version": "1.0.0"
    }

# Si se ejecuta directamente
if __name__ == "__main__":
    import uvicorn
    
    host = "0.0.0.0"
    port = 8001
    
    print(f"Iniciando servidor en http://{host}:{port}")
    print(f"Directorio base: {BASE_DIR}")
    print(f"Documentación: http://localhost:{port}/docs")
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True,
        log_level="info"
    )