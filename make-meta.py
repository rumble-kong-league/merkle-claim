#!/usr/bin/env python
import json


def meta(num: int):
    return {
        "attributes": [{"trait_type": "Sneakers", "value": "Curry Flow"}],
        "image": "ipfs://QmZWjjuu42edcLxoTQbmcUXQcPDrFiH1qmZtqdysjgEeMt",
        "description": "Under Armour x Rumble Kong League celebratory sneaker for all time 3 point record Champion Steph Curry.",
        "name": f"RKL Curry Flow Sneakers #{num}",
    }


def main():
    for i in range(2974):
        m = meta(i + 1)

        with open(f"meta/{i + 1}", "w") as f:
            f.write(json.dumps(m, indent=4))


if __name__ == "__main__":
    main()
