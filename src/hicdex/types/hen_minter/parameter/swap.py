# generated by datamodel-codegen:
#   filename:  swap.json

from __future__ import annotations

from pydantic import BaseModel, Extra


class SwapParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    objkt_amount: str
    objkt_id: str
    xtz_per_objkt: str
