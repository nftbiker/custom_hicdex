# generated by datamodel-codegen:
#   filename:  mint_issuer.json

from __future__ import annotations

from pydantic import BaseModel, Extra


class MintIssuerParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    amount: str
    enabled: bool
    metadata: str
    price: str
    royalties: str
