from brownie import CurryFlow, accounts
from hexbytes import HexBytes


def main():
    a = accounts.load("<account_name>")
    from_a = {"from": a}

    root_hash = HexBytes(
        "0xf5bc31a35860d663e02e7a7f65e121db2e1c60597b9d045b5fcdcf2a4e695a4c"
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
#     HexBytes("e2aaf7e94d9cad66b958f8e20cceea4ca827b9b61d171c07647c5b5801b059f9"),
#     HexBytes("7484cdee31d6583f1e454d48edfd2bec9c107265ab9f474ac5e6dab525af0c92"),
#     HexBytes("171c5aecee0d0bb2b60072a3946de156d4887a98105e2ec4b4645d205e1270c2"),
#     HexBytes("a04f2d2614454afe79d823fad97430a6979c5791992cab4ea75d64259b1cbefb"),
#     HexBytes("b6e7315cb88fe61a22d2dfb4b5819caa4e8f43bc6b9e212e1a36e30cd218e727"),
#     HexBytes("f27dda59f9284c0a27168b600e59fa3bf3ce1b81c4db4d8e10c4f0eebeea066b"),
#     HexBytes("35b75b1e394c95742f3ea46850519c3400f06f53c2c183101e4e547abe1f8403"),
# ]
