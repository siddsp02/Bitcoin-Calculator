# !usr/bin/env python3

import sys
from functools import cache

MAX_SUPPLY = 21_000_000


@cache
def block_reward(block: int, cycled: bool = False) -> float:
    """Calculates the block reward for Bitcoin given the block height."""
    if block < 0:
        raise ValueError("Block height must be positive.")
    return 50 / 2 ** (block // 210_000, block)[cycled]


def circulating_supply(block: int) -> float:
    """Calculates the circulating supply for Bitcoin given the block height."""
    return sum(map(block_reward, range(block + 1)))


def main(block: int = 0) -> None:
    circulating = circulating_supply(block)
    subsidy = block_reward(block)
    print(
        f"At block {block}, the number of circulating bitcoins are {circulating:.8f}",
        f"and the block subsidy is {subsidy:.8f} Bitcoins per block",
    )


if __name__ == "__main__":
    try:
        main(int(sys.argv[1]))
    except IndexError:
        main()
