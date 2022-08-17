from src import *
from src.controller.main import *

from enum import Enum

route = APIRouter(
    prefix="/keuangan",
    default_response_class=JSONResponse,
    tags=["keuangan"],
    responses={404: {"description": "Not found"}},
)


class Menu_Enum(Enum):
    pribadi = "Pribadi"


@route.get("/menu")
def get_menu(db: Session = Depends(get_db)):
    data = get_all_menu(db)
    print(data)
    return JSONResponse({"message": "success", "data": data}, status_code=200)


@route.post("/menu")
async def add_new_menu(request: MenuSchemas, db: Session = Depends(get_db)):
    x = jsonable_encoder(request)

    menu = await add_menu(db, x["name"])
    return JSONResponse({"message": "success", "data": menu}, status_code=status.HTTP_201_CREATED)


@route.delete("/menu/{id}")
def delete_menu_id(id: int, db: Session = Depends(get_db)):
    data = delete_menu(db, id)
    return JSONResponse({"message": "success", "data": data}, status_code=status.HTTP_200_OK)


@route.put("/menu/{id}")
async def update_menu_id(id: int, db: Session = Depends(get_db)):
    menu = await update_menu(db, id)
    return JSONResponse({"message": "success", "data": menu}, status_code=status.HTTP_200_OK)


@route.post("/info_keuangan")
async def add_keuangan(item: AddNewKeungan, db: Session = Depends(get_db)):
    money = await add_info_keuangan(db, item)
    return JSONResponse({"message": "success", "data": money}, status_code=status.HTTP_201_CREATED)


@route.get("/info_keuangan")
def get_infoKeuangan(db: Session = Depends(get_db)):
    data = get_all_info_keuangan(db)
    return JSONResponse({"message": "success", "data": data}, status_code=status.HTTP_200_OK)


@route.get("/")
async def get_all_item(db: Session = Depends(get_db)):
    data = get_all(db)
    return JSONResponse({"message": "success", "data": data}, status_code=status.HTTP_200_OK)


@route.get("/result")
def get_res(menu: Menu_Enum, db: Session = Depends(get_db)):
    print(menu.value)
    data = get_result(db, menu.value)
    return JSONResponse({"message": "success"}, status_code=status.HTTP_200_OK)
