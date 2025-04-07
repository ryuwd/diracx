from __future__ import annotations

from sqlalchemy import (
    Integer,
    Numeric,
    PrimaryKeyConstraint,
    String,
)
from sqlalchemy.orm import DeclarativeBase, mapped_column

from ..utils import DateNowColumn


class JobLoggingDBBase(DeclarativeBase):
    pass


class LoggingInfo(JobLoggingDBBase):
    __tablename__ = "LoggingInfo"
    job_id = mapped_column("JobID", Integer)
    seq_num = mapped_column("SeqNum", Integer)
    status = mapped_column("Status", String(32), default="")
    minor_status = mapped_column("MinorStatus", String(128), default="")
    application_status = mapped_column("ApplicationStatus", String(255), default="")
    status_time = DateNowColumn("StatusTime")
    # TODO: Check that this corresponds to the DOUBLE(12,3) type in MySQL
    status_time_order = mapped_column(
        "StatusTimeOrder", Numeric(precision=12, scale=3), default=0
    )
    source = mapped_column("StatusSource", String(32), default="Unknown")
    __table_args__ = (PrimaryKeyConstraint("JobID", "SeqNum"),)
