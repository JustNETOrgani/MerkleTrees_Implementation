import merkletools
from merkletools import MerkleTools
from hashlib import sha256
import json

myMerkleT = MerkleTools(hash_type="sha256")      # This will make use of SHA256

myMerkleT.add_leaf(["Security", "Room14", "Professor"], True)              #  My first leaves.
myMerkleT.add_leaf(["Room12", "blockchain", "Python"], True)   # This adds three leaves to the Tree.
myMerkleT.add_leaf(["Name:Justice", "Course:Computer Science"], True) # Another three leaves.


myMerkleT.make_tree()      # Creating the Merkle Tree.

print('')
numberOfLeaves = myMerkleT.get_leaf_count()

print("The number of leaves of this tree is: ", numberOfLeaves)

print("root:", myMerkleT.get_merkle_root())  

print("The value at leaf 2 is: ", myMerkleT.get_leaf(2))

print("The array of hash objects for the leaf at index 2 is: ", myMerkleT.get_proof(2))  
                     
print('')
print('************************ Merkle Proof ****************************')
print(myMerkleT.validate_proof(myMerkleT.get_proof(2), myMerkleT.get_leaf(2), myMerkleT.get_merkle_root())) # True
print('************************ Merkle Proof ****************************')

TestData = ["My Professor is helping me to learn well."]

def DataTest(testItem):
    dataPrep = str(json.dumps(TestData))
    testItem = (sha256(dataPrep.encode())).hexdigest()
    return testItem

myHashedData = DataTest(TestData)
print("The Hashed Test Data is: ", myHashedData)

#   Attempting to verify if possible data change can be detected by the Merkle Tree.
#   This would verify whether or not the proof is valid and correctly connects the target_hash
#   in this case the new "myHashedData" to the merkle_root. 
print('')
print('************************ Verification Result ****************************')
print(myMerkleT.validate_proof(myMerkleT.get_proof(2), myHashedData, myMerkleT.get_merkle_root()))
print('')
print('************************ Verification Ends ******************************')