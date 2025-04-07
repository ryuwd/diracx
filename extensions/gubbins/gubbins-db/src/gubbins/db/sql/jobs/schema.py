from diracx.db.sql.job.db import JobDBBase
from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import mapped_column


# You need to inherit from the declarative_base of the parent DB
class GubbinsInfo(JobDBBase):
    """An extra table with respect to Vanilla diracx JobDB"""

    __tablename__ = "GubbinsJobs"

    job_id = mapped_column(
        "JobID", Integer, ForeignKey("Jobs.JobID", ondelete="CASCADE"), primary_key=True
    )
    info = mapped_column("Info", String(255), default="", primary_key=True)
