# generated by datamodel-codegen:
#   filename:  collect_swap.json

from __future__ import annotations

from pydantic import BaseModel, Extra


class CollectSwapParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    amount: str
    swap_id: str
