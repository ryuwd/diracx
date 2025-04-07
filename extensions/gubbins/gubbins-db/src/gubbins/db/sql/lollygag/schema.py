# The utils class define some boilerplate types that should be used
# in place of the SQLAlchemy one. Have a look at them
from diracx.db.sql.utils import DateNowColumn
from sqlalchemy import ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class Owners(Base):
    __tablename__ = "Owners"
    owner_id = mapped_column("OwnerID", Integer, primary_key=True, autoincrement=True)
    creation_time = DateNowColumn("CreationTime")
    name = mapped_column("Name", String(255))


class Cars(Base):
    __tablename__ = "Cars"
    license_plate = mapped_column("LicensePlate", Uuid(), primary_key=True)
    model = mapped_column("Model", String(255))
    owner_id = mapped_column("OwnerID", Integer, ForeignKey(Owners.owner_id))
