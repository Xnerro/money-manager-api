from src import Base, VARCHAR, INTEGER, BOOLEAN, func, relationship, ForeignKey, Column, DATE


class Menu(Base):
    __tablename__ = "Menu"
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(length=255), nullable=False, unique=True)
    is_active = Column(BOOLEAN, default=True)
    created_at = Column(DATE, server_default=func.now())
    updated_at = Column(DATE, default=func.now())

    info_keuangan = relationship("InfoKeuangan", back_populates="menu")

    def __repr__(self):
        return super().__repr__()


class InfoKeuangan(Base):
    __tablename__ = "InfoKeuangan"
    id = Column(INTEGER, primary_key=True)
    id_menu = Column(INTEGER, ForeignKey("Menu.id"))
    description = Column(VARCHAR(length=255))
    is_income = Column(BOOLEAN, default=True)
    is_active = Column(BOOLEAN, default=True)
    created_at = Column(DATE, server_default=func.now())
    updated_at = Column(DATE, default=func.now())

    money = relationship("Money", back_populates="info_keuangan")
    menu = relationship("Menu", back_populates="info_keuangan")

    def __repr__(self):
        return super().__repr__()


class Money(Base):
    __tablename__ = "Money"
    id = Column(INTEGER, primary_key=True)
    id_info_keuangan = Column(INTEGER, ForeignKey("InfoKeuangan.id"))
    nominal = Column(
        INTEGER,
    )
    created_at = Column(DATE, server_default=func.now())
    updated_at = Column(DATE, default=func.now())

    info_keuangan = relationship(InfoKeuangan, back_populates="money")

    def __repr__(self):
        return super().__repr__()
