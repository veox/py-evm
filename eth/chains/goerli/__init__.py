from typing import Tuple, Type  # noqa: F401
from eth_utils import decode_hex

from .constants import (
    GOERLI_CHAIN_ID,
    PETERSBURG_GOERLI_BLOCK,
)
from eth import constants

from eth.chains.base import Chain
from eth.rlp.headers import BlockHeader
from eth.vm.base import BaseVM  # noqa: F401
from eth.vm.forks import PetersburgVM


GOERLI_VM_CONFIGURATION = (
    # Note: Frontier through Constantinople are excluded since this chain starts at Petersburg.
    (PETERSBURG_GOERLI_BLOCK, PetersburgVM),
)


class BaseGoerliChain:
    vm_configuration = GOERLI_VM_CONFIGURATION  # type: Tuple[Tuple[int, Type[BaseVM]], ...]  # noqa: E501
    chain_id = GOERLI_CHAIN_ID  # type: int


class GoerliChain(BaseGoerliChain, Chain):
    pass


GOERLI_GENESIS_HEADER = BlockHeader(
    difficulty=1,
    extra_data=decode_hex("0x22466c6578692069732061207468696e6722202d204166726900000000000000e0a2bd4258d2768837baa26a28fe71dc079f84c70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"),  # noqa: E501
    gas_limit=10485760,
    gas_used=0,
    bloom=0,
    mix_hash=constants.ZERO_HASH32,
    nonce=constants.GENESIS_NONCE,
    block_number=0,
    parent_hash=constants.ZERO_HASH32,
    receipt_root=constants.BLANK_ROOT_HASH,
    uncles_hash=constants.EMPTY_UNCLE_HASH,
    state_root=decode_hex("0x5d6cded585e73c4e322c30c2f782a336316f17dd85a4863b9d838d2d4b8b3008"),
    timestamp=1548854791,
    transaction_root=constants.BLANK_ROOT_HASH,
)
