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

class transactions :
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

class transactions :
    id_sender : str
    id_receiver : str
    amount : str
    signature :str


#Génération des blocs
def create_blockchain(name: str, difficulty: int ):
    bc = blockchain()
    bc.name = name
    bc.n = 0
    bc.chain = []
    bc.difficulty = difficulty
    return bc

# Minage
def is_correct(hash: str, difficulty):
    flag = True
    i = 0
    while i< difficulty :
        if hash[i] != '0' : 
            flag = False
        i = i+1
    return flag

def generate_bloc (index, previous_hash, data, difficulty: int ):
    new = block()
    new.index = index
    new.previous_hash = previous_hash
    new.data = data
    i = 0
    hash = hashlib.sha256( (previous_hash+str(data)+str(i)).encode() )
    proof_of_work = hash.hexdigest()
    while not ( is_correct(str(proof_of_work) , difficulty) ) :
        i = i+1
        proof_of_work = hashlib.sha256( (str(previous_hash)+str(data)+str(i)).encode() ).hexdigest()
    print("Bloc Found")
    print (str(proof_of_work))
    new.proof_of_work = proof_of_work
    return new

def mining (bc: blockchain, data):
    if bc.n >0 :
        last = (bc.chain)[ (bc.n) -1]
        new = generate_bloc(bc.n +1, last.proof_of_work, data, bc.difficulty)
    else :
        new = generate_bloc(0, "0", "Debut", bc.difficulty)
    (bc.chain).append(new)
    bc.n = bc.n +1

#Affichage
def display_bloc (bloc : block):
    print("Index : ",bloc.index)
    print("Previous hash: ",bloc.previous_hash)
    print("Data : ",bloc.data)
    print("Proof of work : ",bloc.proof_of_work,"\n")

def print_blockchain(bc: blockchain):
    print(f"\n{bc.name}")
    print("Difficulty : ", bc.difficulty)
    print(f"Taille de la blockchain : {bc.n}\n")
    i=0
    while (i < bc.n) :      
        display_bloc( bc.chain[i] )
        i=i+1
    print("\nEnd of blockchain")




    
#Gestion des utilisateur
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


#Gestion des transactions :

def create_transactions (receiver, sender, amount):
    new = transactions()
    new.id_receiver = receiver
    new.id_sender = sender
    new.amount = amount

    new.signature

#Main
print("Beginning\n\n")

bc = create_blockchain("Victory", 4)
mining(bc, "Bonjour")
mining(bc, "Bonjour")
mining(bc, "Bonjour")
print_blockchain(bc)
'''

j1 = create_user("GOAT")
display_user(j1)
'''
print("\n\nEnding")