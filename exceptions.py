from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST
from pydantic import ValidationError
from gotrue.errors import AuthApiError  # <-- Import the error type from gotrue

async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "error": "Internal Server Error",
            "message": str(exc),
        },
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": "HTTP Exception",
            "message": exc.detail,
        },
    )

async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": "Validation Error",
            "details": exc.errors(),
        },
    )

# ✅ Add Supabase Auth Error Handler
async def supabase_auth_exception_handler(request: Request, exc: AuthApiError):
    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={
            "success": False,
            "error": "Authentication Failed",
            "message": exc.message,
        },
    )
