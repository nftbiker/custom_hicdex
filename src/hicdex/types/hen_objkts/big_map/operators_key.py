# generated by datamodel-codegen:
#   filename:  operators.key.json

from __future__ import annotations

from pydantic import BaseModel


class OperatorsKey(BaseModel):
    owner: str
    operator: str
    token_id: str
