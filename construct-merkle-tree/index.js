const { MerkleTree } = require("merkletreejs");
const { soliditySha3 } = require("web3-utils");

const keccak256 = (v) => {
  return Buffer.from(soliditySha3(v).slice(2), "hex");
};

const leaves = ["a", "b", "c"].map(keccak256);

const tree = new MerkleTree(leaves, keccak256, { sort: true });
const root = tree.getRoot().toString("hex");
console.log("root:", root);

// const leaf = keccak256("0x00000444e5a1a667663b0ADfD853E8Efa0470698");
// let proof = tree.getProof(leaf);
// console.log(proof.map((e) => e.data.toString("hex")));

// const leaf = keccak256("0xa8e46ded4b92667fe61178299e1063b36351d312");
// let proof = tree.getProof(leaf);
// console.log(tree.verify(proof, leaf, root));
