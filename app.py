from fastapi import FastAPI
from router.router import r
from fastapi.middleware.cors import CORSMiddleware

origins = [
#    "http://localhost.tiangolo.com",
#    "https://localhost.tiangolo.com",
#    "http://localhost",
#    "http://localhost:8080",
    '*'
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(r)

#anyio cffi click cryptography fastapi greenlet h11 idna pycparser pydantic PyMySQL python-dotenv sniffio SQLAlchemy starlette typing-extensions uvicorn