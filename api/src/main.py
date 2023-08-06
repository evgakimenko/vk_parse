import os

from fastapi import FastAPI

from endpoints import vk_parse

app = FastAPI(
    debug=True,
    title="VK_Parse",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.include_router(vk_parse.router)




