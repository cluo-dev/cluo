from enum import Enum


class RunMode(Enum):
    """Modes in which pipelines can be run.  Controls behavior related to sink and offset increment."""

    WRITE = "WRITE"
    PREVIEW = "PREVIEW"
