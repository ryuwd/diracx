from __future__ import annotations

from sqlalchemy import (
    BigInteger,
    Boolean,
    Index,
    Integer,
    PrimaryKeyConstraint,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import DeclarativeBase, mapped_column

from diracx.db.sql.utils import DateNowColumn


class Base(DeclarativeBase):
    pass


class SBOwners(Base):
    __tablename__ = "sb_Owners"
    OwnerID = mapped_column(Integer, autoincrement=True)
    Owner = mapped_column(String(32))
    OwnerGroup = mapped_column(String(32))
    VO = mapped_column(String(64))
    __table_args__ = (PrimaryKeyConstraint("OwnerID"),)


class SandBoxes(Base):
    __tablename__ = "sb_SandBoxes"
    SBId = mapped_column(Integer, autoincrement=True)
    OwnerId = mapped_column(Integer)
    SEName = mapped_column(String(64))
    SEPFN = mapped_column(String(512))
    Bytes = mapped_column(BigInteger)
    RegistrationTime = DateNowColumn()
    LastAccessTime = DateNowColumn()
    Assigned = mapped_column(Boolean, default=False)
    __table_args__ = (
        PrimaryKeyConstraint("SBId"),
        Index("OwnerId", OwnerId),
        UniqueConstraint("SEName", "SEPFN", name="Location"),
    )


class SBEntityMapping(Base):
    __tablename__ = "sb_EntityMapping"
    SBId = mapped_column(Integer)
    EntityId = mapped_column(String(128))
    Type = mapped_column(String(64))
    __table_args__ = (
        PrimaryKeyConstraint("SBId", "EntityId", "Type"),
        Index("SBId", "EntityId"),
        UniqueConstraint("SBId", "EntityId", "Type", name="Mapping"),
    )
