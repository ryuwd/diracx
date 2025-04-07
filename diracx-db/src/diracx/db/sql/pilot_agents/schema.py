from __future__ import annotations

from sqlalchemy import (
    DateTime,
    Double,
    Index,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import DeclarativeBase, mapped_column

from ..utils import EnumBackedBool, NullColumn


class PilotAgentsDBBase(DeclarativeBase):
    pass


class PilotAgents(PilotAgentsDBBase):
    __tablename__ = "PilotAgents"

    pilot_id = mapped_column("PilotID", Integer, autoincrement=True, primary_key=True)
    initial_job_id = mapped_column("InitialJobID", Integer, default=0)
    current_job_id = mapped_column("CurrentJobID", Integer, default=0)
    pilot_job_reference = mapped_column(
        "PilotJobReference", String(255), default="Unknown"
    )
    pilot_stamp = mapped_column("PilotStamp", String(32), default="")
    destination_site = mapped_column(
        "DestinationSite", String(128), default="NotAssigned"
    )
    queue = mapped_column("Queue", String(128), default="Unknown")
    grid_site = mapped_column("GridSite", String(128), default="Unknown")
    vo = mapped_column("VO", String(128))
    grid_type = mapped_column("GridType", String(32), default="LCG")
    benchmark = mapped_column("BenchMark", Double, default=0.0)
    submission_time = NullColumn("SubmissionTime", DateTime)
    last_update_time = NullColumn("LastUpdateTime", DateTime)
    status = mapped_column("Status", String(32), default="Unknown")
    status_reason = mapped_column("StatusReason", String(255), default="Unknown")
    accounting_sent = mapped_column("AccountingSent", EnumBackedBool(), default=False)

    __table_args__ = (
        Index("PilotJobReference", "PilotJobReference"),
        Index("Status", "Status"),
        Index("Statuskey", "GridSite", "DestinationSite", "Status"),
    )


class JobToPilotMapping(PilotAgentsDBBase):
    __tablename__ = "JobToPilotMapping"

    pilot_id = mapped_column("PilotID", Integer, primary_key=True)
    job_id = mapped_column("JobID", Integer, primary_key=True)
    start_time = mapped_column("StartTime", DateTime)

    __table_args__ = (Index("JobID", "JobID"), Index("PilotID", "PilotID"))


class PilotOutput(PilotAgentsDBBase):
    __tablename__ = "PilotOutput"

    pilot_id = mapped_column("PilotID", Integer, primary_key=True)
    std_output = mapped_column("StdOutput", Text)
    std_error = mapped_column("StdError", Text)
