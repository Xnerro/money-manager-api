from typing import Optional
from src import Session, func, HTTPException
from src.model.model import Menu, InfoKeuangan, Money
from src.schemas.main import *


def get_all_menu(db: Session):
    menu = db.query(Menu).all()
    data: list = []
    for m in menu:
        data.append(
            {
                "id": m.id,
                "name": m.name,
                "is_active": m.is_active,
            }
        )
    return data


def get_all_info_keuangan(db: Session):
    info_keuangan = db.query(InfoKeuangan).all()
    data: list = []
    for i in info_keuangan:
        data.append(
            {
                "id": i.id,
                "menu_id": i.id_menu,
                "description": i.description,
                "is_income": i.is_income,
            }
        )
    return data


def get_all_money(db: Session):
    money = db.query(Money)
    data: list = []
    for m in money:
        data.append(
            {
                "id": m.id,
                "id_info_keuangan": m.id_info_keuangan,
                "nominals": m.nominal,
            }
        )
    return data


async def add_menu(db: Session, name: str):
    menu = Menu(name=name, is_active=True)
    db.add(menu)
    db.commit()
    data = {
        "id": menu.id,
        "name": menu.name,
        "is_active": menu.is_active,
    }
    return data


async def add_info_keuangan(db: Session, item: AddNewKeungan):
    if db.query(Menu).filter(Menu.id == item.id_menu).first() is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    new_info = InfoKeuangan(
        id_menu=item.id_menu, description=item.description, is_income=item.is_income, is_active=item.is_active
    )
    db.add(new_info)
    db.commit()
    db.refresh(new_info)
    new_money = Money(nominal=item.nominal, id_info_keuangan=new_info.id)
    db.add(new_money)
    db.commit()
    db.refresh(new_money)
    data = {
        "id": new_info.id,
        "id_menu": new_info.id_menu,
        "description": new_info.description,
        "is_income": new_info.is_income,
        "is_active": new_info.is_active,
        "nominal": new_money.nominal,
        "id_info_keuangan": new_money.id_info_keuangan,
    }
    return data


def get_money(db: Session, id: int):
    money = db.query(Money).filter(Money.id_info_keuangan == id).first()
    return {
        "id": money.id,
        "id_info_keuangan": money.id_info_keuangan,
        "nominal": money.nominal,
    }


def delete_menu(db: Session, id: int):
    menu = db.query(Menu).filter(Menu.id == id).first()
    db.delete(menu)
    db.commit()
    data = {
        "id": menu.id,
        "name": menu.name,
        "is_active": menu.is_active,
    }
    return data


async def update_menu(db: Session, id: int):
    menu = db.query(Menu).filter(Menu.id == id).first()
    if menu.is_active:
        menu.is_active = False
    else:
        menu.is_active = True
    db.merge(menu)
    db.commit()
    return {
        "id": menu.id,
        "name": menu.name,
        "is_active": menu.is_active,
    }


def get_all(db: Session):
    item = db.query(InfoKeuangan, Money).join(Money).all()
    data: list = []
    for x in item:
        data.append(
            {
                "id": x[0].id,
                "is_active": x[0].is_active,
                "description": x[0].description,
                "is_income": x[0].is_income,
                "nominal": x[1].nominal,
                "id_menu": x[0].id_menu,
            }
        )
    return data


def get_result(db: Session, menu: int):
    item = (
        db.query(func.sum(Money.nominal), func.max(Money.nominal), func.min(Money.nominal))
        .join(InfoKeuangan)
        .join(Menu)
        .filter(InfoKeuangan.is_income == True, Menu.name == menu)
        .first()
    )
    print(item)
    return
