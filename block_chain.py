#coding utf-8


#Importation des librairies
import hashlib
import cryptography
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

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
    public_key : cryptography.hazmat.primitives.asymmetric.rsa.RSAPublicKey
    private_key : cryptography.hazmat.primitives.asymmetric.rsa.RSAPrivateKey
    wallet : int

class transactions :
    id_transaction : str
    sender : str
    receiver : str
    amount : int
    nonce :str


#------Gestion des blocs-----------------------#

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



#------Gestion des utilisateurs-----------------------#

def create_user (name, wallet):
    new = user()
    new.name = name
    new.wallet = wallet
    privkey = rsa.generate_private_key(public_exponent=65537, key_size=2048 )
    new.private_key = privkey
    new.public_key = privkey.public_key()
    return new

def display_user(user : user):
    print("User: ", user.name)
    print("Wallet: ", user.wallet)
    print("Public key: ", user.public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo))
    print("Private key: ", user.private_key.private_bytes( encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption() ))
    print("\n\n")

def display_user_list( l_user ):
    l_cpy = l_user.copy()
    while(l_cpy!= []):
        display_user(l_cpy.pop(0))


#------Gestion des utilisateurs-----------------------#

def create_transactions (id_transaction, receiver: user, sender: user, amount):
    new = transactions()
    new.id_transaction = id_transaction
    new.receiver = receiver
    new.sender = sender
    new.amount = amount
    message = b"HELLO"
    new.nonce = sender.private_key.sign( message, padding.PSS( mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256() )  
    return new

def display_transaction ( transaction :transactions):
    print("Transaction id : ", transaction.id_transaction)
    print("From :")
    display_user(transaction.sender)
    print("To: ")
    display_user(transaction.receiver)
    print("\nAmount: ", transaction.amount)
    print("Signature: ", transaction.nonce, "\n\n")

def check_transaction_conditions(sender: user, sum : int):
    flag = True
    if sender.wallet < sum :
         flag = False
    return flag


def make_transaction(id_transaction, receiver: user, sender: user, amount: int):
    if check_transaction_conditions(sender , amount ):
        sender.wallet = (sender.wallet) - amount
        receiver.wallet = (receiver.wallet) + amount 
        print("Transaction Done")

        return create_transactions(id_transaction, receiver, sender, amount)
    else :
        print("Transaction refusée")
        return None



#------Gestion de l'interface-----------------------#

def init():
    #Création de la BlockChain
    print("Choisis un nom de BlockChain")
    name = input()
    print("Choisis une difficulté de BlockChain")
    difficulty = int(input())
    bc = create_blockchain(name, difficulty)

    #Création des utilisateurs
    user_list = []
    print("\nChoisis un nombre d'utilisateur")
    nb_user = int(input())
    while nb_user> 0: 
        print("\nChoisis le nom de l'utilisateur", nb_user)
        name = input()
        print("Choisis le montant possédé par l'utilisateur", nb_user)
        found = int(input())
        user_list.append(create_user(name, found))
        nb_user = nb_user-1
    display_user_list(user_list)



    


#Main
print("Beginning\n\n")
init()
'''
init()
bc = create_blockchain("Victory", 4)
mining(bc, "Bonjour")
mining(bc, "Bonjour")
mining(bc, "Bonjour")
print_blockchain(bc)


j1 = create_user("Maya", 60)
j2 = create_user("Léon", 70)


trans_1 = make_transaction("trans_1", j1, j2, 50)
display_transaction(trans_1)

display_user(j1)
display_user(j2)
'''
print("\n\nEnding")