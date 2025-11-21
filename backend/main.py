from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from dotenv import load_dotenv

# 載入 .env 檔案
load_dotenv()

from database import Base, init_engine, get_engine
import models
import auth

app = FastAPI()

ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://resrv.vercel.app",
    "https://resrv-frontend.vercel.app",
    "https://*.vercel.app",  # 支援所有 Vercel 子網域
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.get("/")
def root():
    return {"msg": "Backend running successfully!"}

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return {}, 204


@app.on_event("startup")
def on_startup():
    try:
        init_engine()
        Base.metadata.create_all(bind=get_engine())
    except Exception as e:
        print(f"⚠️  資料庫初始化警告: {e}")
        # 在 Serverless 環境中，資料庫可能無法立即初始化，這是正常的

# Routers
app.include_router(auth.router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Resrv API",
        version="1.0.0",
        description="Resrv authentication and restaurant APIs",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", [{"BearerAuth": []}])
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
