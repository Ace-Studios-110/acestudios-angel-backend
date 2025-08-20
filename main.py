# import logging
# logging.basicConfig(level=logging.DEBUG)
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from gotrue.errors import AuthApiError

# Routers
from routers.auth_router import auth_router
from routers.angel_router import router as angel_router

# Middlewares
from middlewares.auth import verify_auth_token

# Exceptions
from exceptions import (
    global_exception_handler,
    validation_exception_handler,
    http_exception_handler,
    supabase_auth_exception_handler,
)

app = FastAPI(title="Founderport Angel Assistant")

# ✅ Root route for health check
@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "Founderport Angel Assistant API is running",
        "version": "1.0.0"
    }

# ✅ CORS Support
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Routers
app.include_router(auth_router, prefix="/auth")
app.include_router(angel_router, prefix="/angel")

# ✅ Global Exception Handlers
app.add_exception_handler(AuthApiError, supabase_auth_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
