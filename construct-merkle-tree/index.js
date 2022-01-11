const { MerkleTree } = require("merkletreejs");
const { soliditySha3 } = require("web3-utils");
const snapshot = require("./snapshot.json");

// * soliditySha3 acts as abi.encodePacked
// * See: https://blog.8bitzen.com/posts/18-03-2019-keccak-abi-encodepacked-with-javascript/
const keccak256 = (...x) => {
  return Buffer.from(soliditySha3(...x).slice(2), "hex");
};

const leaves = snapshot.map((x) => keccak256(x.address, x.quantity));
const tree = new MerkleTree(leaves, keccak256, { sort: true });

const root = tree.getRoot().toString("hex");
const leaf = keccak256("0x66aB6D9362d4F35596279692F0251Db635165871", 32);
let proof = tree.getProof(leaf);

console.log("root:", root);
console.log(
  "proof:",
  proof.map((e) => e.data.toString("hex"))
);
console.log("verified:", tree.verify(proof, leaf, root));
