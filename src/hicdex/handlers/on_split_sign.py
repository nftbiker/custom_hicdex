import hicdex.models as models
from dipdup.context import HandlerContext
from dipdup.models import Transaction
from hicdex.types.split_sign.parameter.sign import SignParameter
from hicdex.types.split_sign.storage import SplitSignStorage


async def on_split_sign(
    ctx: HandlerContext,
    sign: Transaction[SignParameter, SplitSignStorage],
) -> None:
    sender = sign.data.sender_address
    objkt_id = sign.parameter.__root__

    token, _ = await models.Token.get_or_create(id=str(objkt_id), fa2_id='KT1RJ6PbjHpwc3M5rw5s2Nbmefwbuwbdxton')
    # type: ignore
    contract, _ = await models.SplitContract.get_or_create(contract_id=token.creator_id)

    await models.Signatures.get_or_create(holder_id=sender, token_id=token.pk_id)

    try:
        core_participants = await models.Shareholder.filter(
            split_contract=contract, holder_type=models.ShareholderStatus.core_participant
        ).all()
        # type: ignore
        sig_required = {
            shareholder.holder_id for shareholder in core_participants}
        signers = await models.Signatures.filter(token=token).all()
        sig_created = {signer.holder_id for signer in signers}  # type: ignore

        if sig_required.issubset(sig_created):
            token.is_signed = True  # type: ignore
            await token.save()
    except:
        return
