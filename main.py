# FastAPI application startup script
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.staticfiles import StaticFiles

from fastapi.openapi.utils import get_openapi
from JIRA.routers import tickets

origins = [
    "http://localhost:3000/",
    "http://localhost:8010",
]


app = FastAPI(debug=True)


# Define your custom logo image URL
custom_logo_url = "https://cdn0.iconfinder.com/data/icons/find-a-job-and-interview-flat/512/business_infographic_marketing_report_slide_corporate_presentation_graph_powerpoint-1024.png"


# Customize the Swagger UI HTML template to include the custom logo
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="JIRA Integration",
        description="Fast, seamless Jira integration APIs for streamlined project management.",
        version="0.0.1",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {"url": custom_logo_url}
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SessionMiddleware, secret_key="some-random-string")
app.include_router(tickets.jira_routes, tags=["Ticket Managements"])


# Your routes go here
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8010)
