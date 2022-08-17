from __init__ import *


@app.get("/")
async def root():
    return RedirectResponse("/docs", status_code=302)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
