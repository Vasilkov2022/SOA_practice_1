from fastapi import FastAPI, Request
import uvicorn
import os
import requests
from fastapi.responses import JSONResponse, Response

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://localhost:8001")

app = FastAPI(
    title="Proxy Service",
    version="1.0.0"
)

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy(request: Request, path: str):
    """
    Универсальное проксирование запросов на User Service.
    Все запросы по любому пути -> идут на http://user_service:8001/{path}.
    """
    url = f"{USER_SERVICE_URL}/{path}"
    # Собираем запрос:
    # 1) method
    # 2) headers
    # 3) body
    method = request.method
    headers = dict(request.headers)
    body = await request.body()

    # Прокидываем запрос в User Service
    try:
        resp = requests.request(method, url, headers=headers, data=body, timeout=10)
        return Response(content=resp.content, status_code=resp.status_code, headers={
            # Можно прокинуть нужные заголовки
            "Content-Type": resp.headers.get("Content-Type", "application/json")
        })
    except requests.RequestException as e:
        return JSONResponse(
            status_code=500,
            content={"detail": f"Proxy error: {str(e)}"}
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)