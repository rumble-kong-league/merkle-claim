// SPDX-License-Identifier: MIT
pragma solidity =0.8.11;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";

import "./MerkleProof.sol";

error AlreadyClaimed(address account);

error InvalidProof();

error NotAdmin(address account);

// todo: docs

contract CurryFlow is ERC721Enumerable {
    bytes32 public immutable merkleRoot;
    mapping(uint256 => uint256) private claimedBitMap;

    uint256 private currentTokenIndex = 1;
    address private owner;
    string private uri;

    constructor(
        string memory name_,
        string memory symbol_,
        bytes32 merkleRoot_
    ) ERC721(name_, symbol_) {
        merkleRoot = merkleRoot_;
        owner = msg.sender;
    }

    function claim(
        address account,
        uint256 qty,
        bytes32[] calldata merkleProof
    ) external {
        if (isClaimed(uint256(uint160(account)))) {
            revert AlreadyClaimed(account);
        }

        bytes32 node = keccak256(abi.encodePacked(account, qty));

        if (!MerkleProof.verify(merkleProof, merkleRoot, node)) {
            revert InvalidProof();
        }

        _setClaimed(uint256(uint160(account)));

        for (uint256 i = 0; i < qty; i++) {
            _safeMint(account, currentTokenIndex);
            currentTokenIndex += 1;
        }
    }

    function isClaimed(uint256 index) public view returns (bool) {
        uint256 claimedWord = claimedBitMap[index / 256];
        uint256 mask = (1 << (index % 256));
        return claimedWord & mask == mask;
    }

    function _setClaimed(uint256 index) private {
        uint256 claimedWordIndex = index / 256;
        claimedBitMap[claimedWordIndex] =
            claimedBitMap[claimedWordIndex] |
            (1 << (index % 256));
    }

    function _baseURI() internal view override returns (string memory) {
        return uri;
    }

    function setURI(string calldata uri_) external {
        if (msg.sender != owner) {
            revert NotAdmin(msg.sender);
        }

        uri = uri_;
    }

    function revokeOwnership() external {
        if (msg.sender != owner) {
            revert NotAdmin(msg.sender);
        }

        owner = address(0);
    }
}
