# App mínima de arranque, solo para verificar que el contenedor levanta y responde.
# Aquí va, en realidad, la lógica real del proyecto.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PEREDENT")

# CORS abierto para desarrollo; cerrar en producción a los orígenes reales.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "PEREDENT running"}

@app.get("/health")   # endpoint simple para chequear que la app está viva
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
