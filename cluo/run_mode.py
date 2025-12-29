from enum import Enum


class RunMode(Enum):
    """Modes in which pipelines can be run.  Controlls behavior related to sink and offset increment."""

    WRITE = "WRITE"
    PREVIEW = "PREVIEW"
