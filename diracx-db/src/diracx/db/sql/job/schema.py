from __future__ import annotations

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import DeclarativeBase, mapped_column

from ..utils import EnumBackedBool, NullColumn


class JobDBBase(DeclarativeBase):
    pass


class Jobs(JobDBBase):
    __tablename__ = "Jobs"

    job_id = mapped_column(
        "JobID",
        Integer,
        ForeignKey("JobJDLs.JobID", ondelete="CASCADE"),
        primary_key=True,
        default=0,
    )
    job_type = mapped_column("JobType", String(32), default="user")
    job_group = mapped_column("JobGroup", String(32), default="00000000")
    site = mapped_column("Site", String(100), default="ANY")
    job_name = mapped_column("JobName", String(128), default="Unknown")
    owner = mapped_column("Owner", String(64), default="Unknown")
    owner_group = mapped_column("OwnerGroup", String(128), default="Unknown")
    vo = mapped_column("VO", String(32))
    submission_time = NullColumn("SubmissionTime", DateTime)
    reschedule_time = NullColumn("RescheduleTime", DateTime)
    last_update_time = NullColumn("LastUpdateTime", DateTime)
    start_exec_time = NullColumn("StartExecTime", DateTime)
    heart_beat_time = NullColumn("HeartBeatTime", DateTime)
    end_exec_time = NullColumn("EndExecTime", DateTime)
    status = mapped_column("Status", String(32), default="Received")
    minor_status = mapped_column("MinorStatus", String(128), default="Unknown")
    application_status = mapped_column(
        "ApplicationStatus", String(255), default="Unknown"
    )
    user_priority = mapped_column("UserPriority", Integer, default=0)
    reschedule_counter = mapped_column("RescheduleCounter", Integer, default=0)
    verified_flag = mapped_column("VerifiedFlag", EnumBackedBool(), default=False)
    # TODO: Should this be True/False/"Failed"? Or True/False/Null?
    accounted_flag = mapped_column(
        "AccountedFlag", Enum("True", "False", "Failed"), default="False"
    )

    __table_args__ = (
        Index("JobType", "JobType"),
        Index("JobGroup", "JobGroup"),
        Index("Site", "Site"),
        Index("Owner", "Owner"),
        Index("OwnerGroup", "OwnerGroup"),
        Index("Status", "Status"),
        Index("MinorStatus", "MinorStatus"),
        Index("ApplicationStatus", "ApplicationStatus"),
        Index("StatusSite", "Status", "Site"),
        Index("LastUpdateTime", "LastUpdateTime"),
    )


class JobJDLs(JobDBBase):
    __tablename__ = "JobJDLs"
    job_id = mapped_column("JobID", Integer, autoincrement=True, primary_key=True)
    jdl = mapped_column("JDL", Text)
    job_requirements = mapped_column("JobRequirements", Text)
    original_jdl = mapped_column("OriginalJDL", Text)


class InputData(JobDBBase):
    __tablename__ = "InputData"
    job_id = mapped_column(
        "JobID", Integer, ForeignKey("Jobs.JobID", ondelete="CASCADE"), primary_key=True
    )
    lfn = mapped_column("LFN", String(255), default="", primary_key=True)
    status = mapped_column("Status", String(32), default="AprioriGood")


class JobParameters(JobDBBase):
    __tablename__ = "JobParameters"
    job_id = mapped_column(
        "JobID", Integer, ForeignKey("Jobs.JobID", ondelete="CASCADE"), primary_key=True
    )
    name = mapped_column("Name", String(100), primary_key=True)
    value = mapped_column("Value", Text)


class OptimizerParameters(JobDBBase):
    __tablename__ = "OptimizerParameters"
    job_id = mapped_column(
        "JobID", Integer, ForeignKey("Jobs.JobID", ondelete="CASCADE"), primary_key=True
    )
    name = mapped_column("Name", String(100), primary_key=True)
    value = mapped_column("Value", Text)


class AtticJobParameters(JobDBBase):
    __tablename__ = "AtticJobParameters"
    job_id = mapped_column(
        "JobID", Integer, ForeignKey("Jobs.JobID", ondelete="CASCADE"), primary_key=True
    )
    name = mapped_column("Name", String(100), primary_key=True)
    value = mapped_column("Value", Text)
    reschedule_cycle = mapped_column("RescheduleCycle", Integer)


class HeartBeatLoggingInfo(JobDBBase):
    __tablename__ = "HeartBeatLoggingInfo"
    job_id = mapped_column(
        "JobID", Integer, ForeignKey("Jobs.JobID", ondelete="CASCADE"), primary_key=True
    )
    name = mapped_column("Name", String(100), primary_key=True)
    value = mapped_column("Value", Text)
    heart_beat_time = mapped_column("HeartBeatTime", DateTime, primary_key=True)


class JobCommands(JobDBBase):
    __tablename__ = "JobCommands"
    job_id = mapped_column(
        "JobID", Integer, ForeignKey("Jobs.JobID", ondelete="CASCADE"), primary_key=True
    )
    command = mapped_column("Command", String(100))
    arguments = mapped_column("Arguments", String(100))
    status = mapped_column("Status", String(64), default="Received")
    reception_time = mapped_column("ReceptionTime", DateTime, primary_key=True)
    execution_time = NullColumn("ExecutionTime", DateTime)
