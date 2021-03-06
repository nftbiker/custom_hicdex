# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Dict

from pydantic import BaseModel, Extra


class FxhashUserStorage(BaseModel):
    class Config:
        extra = Extra.forbid

    admin: str
    metadata: Dict[str, str]
    names_taken: Dict[str, bool]
    users_metadata: Dict[str, str]
    users_name: Dict[str, str]
