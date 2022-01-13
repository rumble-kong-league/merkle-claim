from brownie import CurryFlow, accounts
from hexbytes import HexBytes


def main():
    a = accounts.load("<your account name>")
    from_a = {"from": a}

    root_hash = HexBytes(
        "0x7958644db5b336dc022fe122ff9342c8e461a4e6533fb32cd9f8dc65eaecade4"
    )

    # This deploys curry flow merkle ERC721 contract
    cf = CurryFlow.deploy("Rumble Kong League Curry Flow", "RKLCF", root_hash, from_a)

    # If already deployed, use this to get an instance.
    # cf = CurryFlow.at(address, owner=a)


if __name__ == "__main__":
    main()

# This is used to copy and paste into brownie console when testing the contract (validity of proofs)
# To obtain these proofs, use `index.js` in `construct-merkle-tree/`
# proof = [
#     HexBytes("702c067b511a19446d86e5810d31312aaf266c8fa0f9defe675687f5bd29f926"),
#     HexBytes("459cc03f11470f406b801e8c5a8e7ee1edfcb07440d9d14407622aa075d73af3"),
#     HexBytes("721be47c8a69e21ac5fc30cb646cf7428007c339ddc40609620e9e97c4e3b47c"),
#     HexBytes("11697a9535f60df81b433259aaf49cb4db68122227c47af90dafa708eb3cc67e"),
#     HexBytes("3ddd5ece6835609d29fa96ce72e566bc0b65b15c77b56e296fb37c24bd278a4a"),
#     HexBytes("422b4b964ef1405417b8852ba6104883596cf6edf351ae0f8f3a703aeea09fc9"),
#     HexBytes("42073b4b6a6c61e49869aaba1722599239c22c7fe9116c7fc1f297b8b2068b91"),
#     HexBytes("f2a3a025b94ab346e79a56f8c919a9c786e8ce6fdf537be92f21a0d16fb104b4"),
#     HexBytes("f2060a71130c7bcb97e43c5de7a3d0467c4a512e2ffae79ea2f85c7db9e8cf56"),
#     HexBytes("045c94ff925c041498a183f977ca5b8ec69f1b0427acfb1e92cd47cff4e85b0f"),
#     HexBytes("78f7aaee797d5dda64c4d877493136f457d3df992793608b1104e5fd0500b6c9"),
#     HexBytes("b5ced62e1befa4768c7bb962a16e89b72f7841c9d3afe8bd6e38bb669f933c00"),
# ]
