#coding utf-8

import hashlib


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
    signature :str
    proof_of_work : str

class blockchain:
    name: str
    n :int
    chain : list

class user :
    name : str
    public_key : str
    private_key : str

#Génération des blocs
def generate_bloc (index, previous_hash, signature, data):
    new = block()
    new.index = index
    new.previous_hash = previous_hash
    new.data = data
    new.signature = signature
    new.proof_of_work = hashlib.sha256( (str(previous_hash)+str(data)+str(signature)).encode() )
    return new

def display_bloc (bloc : block):
    print("Index : ",bloc.index)
    print("Previous hash: ",bloc.previous_hash)
    print("Data : ",bloc.data)
    print("Signature : ",bloc.signature)
    print("Proof of work : ",bloc.proof_of_work,"\n")

def create_blockchain(name: str):
    bc = blockchain()
    bc.name = name
    bc.n = 0
    bc.chain = []
    return bc

def add_block(bc : blockchain , bloc : block):
    (bc.chain).append(bloc)
    bc.n = bc.n +1

def mining (bc: blockchain):
    if bc.n >0 :
        last = (bc.chain)[ (bc.n) -1]
        new = generate_bloc(bc.n, last.proof_of_work, "Me", "Bonjour")
    else :
        new = generate_bloc(0, "0", "Me", "Debut")
    add_block(bc, new)

def print_blockchain(bc: blockchain):
    print(f"{bc.name}")
    print(f"Taille de la blockchain : {bc.n}\n")
    i=0
    while (i < bc.n) :      
        display_bloc( bc.chain[i] )
        i=i+1
    print("\nEnd of blockchain")
    
#Gestion des utilisateur
'''
def create_user ():
    new = user()
    return new

def set_up_user (name: str ): #inculuding key generation
    new = create_user()
    new.name = name

'''



#Main
print("Beginning\n\n")

'''a = generate_bloc(0, "azerty", "To me")
display_bloc(a)
'''

bc = create_blockchain("Victory")
mining(bc)
mining(bc)
mining(bc)
mining(bc)
print_blockchain(bc)

print("\n\nEnding")