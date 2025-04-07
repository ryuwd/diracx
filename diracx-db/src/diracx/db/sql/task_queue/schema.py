from __future__ import annotations

from sqlalchemy import (
    BigInteger,
    Boolean,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
)
from sqlalchemy.orm import DeclarativeBase, mapped_column


class TaskQueueDBBase(DeclarativeBase):
    pass


class TaskQueues(TaskQueueDBBase):
    __tablename__ = "tq_TaskQueues"
    TQId = mapped_column(Integer, primary_key=True)
    Owner = mapped_column(String(255), nullable=False)
    OwnerGroup = mapped_column(String(32), nullable=False)
    VO = mapped_column(String(32), nullable=False)
    CPUTime = mapped_column(BigInteger, nullable=False)
    Priority = mapped_column(Float, nullable=False)
    Enabled = mapped_column(Boolean, nullable=False, default=0)
    __table_args__ = (Index("TQOwner", "Owner", "OwnerGroup", "CPUTime"),)


class JobsQueue(TaskQueueDBBase):
    __tablename__ = "tq_Jobs"
    TQId = mapped_column(
        Integer, ForeignKey("tq_TaskQueues.TQId", ondelete="CASCADE"), primary_key=True
    )
    JobId = mapped_column(Integer, primary_key=True)
    Priority = mapped_column(Integer, nullable=False)
    RealPriority = mapped_column(Float, nullable=False)
    __table_args__ = (Index("TaskIndex", "TQId"),)


class SitesQueue(TaskQueueDBBase):
    __tablename__ = "tq_TQToSites"
    TQId = mapped_column(
        Integer, ForeignKey("tq_TaskQueues.TQId", ondelete="CASCADE"), primary_key=True
    )
    Value = mapped_column(String(64), primary_key=True)
    __table_args__ = (
        Index("SitesTaskIndex", "TQId"),
        Index("SitesIndex", "Value"),
    )


class GridCEsQueue(TaskQueueDBBase):
    __tablename__ = "tq_TQToGridCEs"
    TQId = mapped_column(
        Integer, ForeignKey("tq_TaskQueues.TQId", ondelete="CASCADE"), primary_key=True
    )
    Value = mapped_column(String(64), primary_key=True)
    __table_args__ = (
        Index("GridCEsTaskIndex", "TQId"),
        Index("GridCEsValueIndex", "Value"),
    )


class BannedSitesQueue(TaskQueueDBBase):
    __tablename__ = "tq_TQToBannedSites"
    TQId = mapped_column(
        Integer, ForeignKey("tq_TaskQueues.TQId", ondelete="CASCADE"), primary_key=True
    )
    Value = mapped_column(String(64), primary_key=True)
    __table_args__ = (
        Index("BannedSitesTaskIndex", "TQId"),
        Index("BannedSitesValueIndex", "Value"),
    )


class PlatformsQueue(TaskQueueDBBase):
    __tablename__ = "tq_TQToPlatforms"
    TQId = mapped_column(
        Integer, ForeignKey("tq_TaskQueues.TQId", ondelete="CASCADE"), primary_key=True
    )
    Value = mapped_column(String(64), primary_key=True)
    __table_args__ = (
        Index("PlatformsTaskIndex", "TQId"),
        Index("PlatformsValueIndex", "Value"),
    )


class JobTypesQueue(TaskQueueDBBase):
    __tablename__ = "tq_TQToJobTypes"
    TQId = mapped_column(
        Integer, ForeignKey("tq_TaskQueues.TQId", ondelete="CASCADE"), primary_key=True
    )
    Value = mapped_column(String(64), primary_key=True)
    __table_args__ = (
        Index("JobTypesTaskIndex", "TQId"),
        Index("JobTypesValueIndex", "Value"),
    )


class TagsQueue(TaskQueueDBBase):
    __tablename__ = "tq_TQToTags"
    TQId = mapped_column(
        Integer, ForeignKey("tq_TaskQueues.TQId", ondelete="CASCADE"), primary_key=True
    )
    Value = mapped_column(String(64), primary_key=True)
    __table_args__ = (
        Index("TagsTaskIndex", "TQId"),
        Index("TagsValueIndex", "Value"),
    )
