#coding utf-8

import hashlib

import rsa



#Définition des structures
class block :
    pass

class blockchain:
    pass

class user :
    pass

class block :
    index : int
    previous_hash : str
    data : str
    proof_of_work : str

class blockchain:
    name: str
    n :int
    chain : list
    difficulty : int

class user :
    name : str
    public_key : str
    private_key : str

#Génération des blocs
def generate_bloc (index, previous_hash, data):
    new = block()
    new.index = index
    new.previous_hash = previous_hash
    new.data = data
    new.proof_of_work = hashlib.sha256( (str(previous_hash)+str(data)).encode() )
    return new

def display_bloc (bloc : block):
    print("Index : ",bloc.index)
    print("Previous hash: ",bloc.previous_hash)
    print("Data : ",bloc.data)
    print("Proof of work : ",bloc.proof_of_work,"\n")

def create_blockchain(name: str, difficulty: int ):
    bc = blockchain()
    bc.name = name
    bc.n = 0
    bc.chain = []
    bc.difficulty = difficulty
    return bc

def add_block(bc : blockchain , bloc : block):
    (bc.chain).append(bloc)
    bc.n = bc.n +1

def mining (bc: blockchain):
    if bc.n >0 :
        last = (bc.chain)[ (bc.n) -1]
        new = generate_bloc(bc.n, last.proof_of_work, "Bonjour")
    else :
        new = generate_bloc(0, "0", "Debut")
    add_block(bc, new)

def print_blockchain(bc: blockchain):
    print(f"{bc.name}")
    print("Difficulty : ", bc.difficulty)
    print(f"Taille de la blockchain : {bc.n}\n")
    i=0
    while (i < bc.n) :      
        display_bloc( bc.chain[i] )
        i=i+1
    print("\nEnd of blockchain")
    
#Gestion des utilisateur

def create_key():
    
    return privkey, pubkey


def create_user (name):
    new = user()
    new.name = name
    (pubkey, privkey) = rsa.newkeys(1024)
    new.private_key = privkey
    new.public_key = pubkey
    return new


def display_user(user : user):
    print("User: ", user.name)
    print("Public key: ", user.public_key)
    print("Private key: ", user.private_key)



#Main
print("Beginning\n\n")



bc = create_blockchain("Victory", 4)
mining(bc)
mining(bc)
mining(bc)
mining(bc)
print_blockchain(bc)

j1 = create_user("GOAT")
display_user(j1)

print("\n\nEnding")