import sys

BASE_REWARD = 50
REDUCTION = 1 / 2
INTERVAL = 210_000
MAX_SUPPLY = 21_000_000


def block_reward(height: int) -> float:
    """Calculates the block reward for Bitcoin given the block height."""
    return BASE_REWARD * REDUCTION ** (height // INTERVAL)


def circulating_supply(height: int) -> float:
    """Calculates the circulating supply of Bitcoin given the block height."""

    if height < 0:
        raise ValueError("Height must be a non-negative integer.")
        
    if not isinstance(height, int):
        raise TypeError("Height must be an integer.")

    height += 1
    halving_cycles = height // INTERVAL

    return BASE_REWARD * REDUCTION ** halving_cycles * (
        height / INTERVAL - halving_cycles
    ) * INTERVAL + sum(
        MAX_SUPPLY * REDUCTION ** x for x in range(1, halving_cycles + 1)
    )


def main(block: int) -> None:
    circulating = circulating_supply(block)
    subsidy = block_reward(block)
    print(
        f"At block {block:d}, the number of circulating bitcoins are {circulating:.8f}",
        f"and the block subsidy is {subsidy:.8f} Bitcoins per block",
    )


if __name__ == "__main__":
    main(int(sys.argv[1]))
