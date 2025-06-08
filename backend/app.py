from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

def create_app() -> FastAPI:
    
     
    app = FastAPI(title="Notes API",
                  description="API beckaned for personal notes.",
                  version="1.0.0")
    
    
    app.add_middleware(CORSMiddleware, 
                       allow_origins=["*"],
                       allow_credentials=True,
                       allow_methods={"*"},
                       allow_headers=["*"])

    
    
    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="127.0.0.1", port="5000")