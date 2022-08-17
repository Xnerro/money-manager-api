from src import BaseModel


class MenuSchemas(BaseModel):
    name: str
    is_active: bool


class InfoKeuanganSchemas(BaseModel):
    id_menu: int
    description: str
    is_income: bool
    is_active: bool


class MoneySchemas(BaseModel):
    nominal: int
    id_info_keuangan: int


class AddNewKeungan(BaseModel):
    id_menu: int
    description: str
    is_income: bool
    is_active: bool
    nominal: int
