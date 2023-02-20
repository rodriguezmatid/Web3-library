import hashlib
import time
import random

# Implementación de una función de hash SHA-256
# https://docs.python.org/3/library/hashlib.html
def hash_sha256(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode()) # Update the hash object with the bytes-like object. The encode() method encodes the string, using the specified encoding
    return sha256.hexdigest() # Like digest() except the digest is returned as a string object of double length, containing only hexadecimal digits. This may be used to exchange the value safely in email or other non-binary environments.

data = "Hello World!"
print("Data: ", data)
print("Hash: ", hash_sha256(data))
print()

# Creación de un bloque básico
class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha256 = hashlib.sha256()
        sha256.update((str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode())
        return sha256.hexdigest()

block = Block("Hello World!", "0")
print("Timestamp: ", block.timestamp)
print("Data: ", block.data)
print("Previous Hash: ", block.previous_hash)
print("Hash: ", block.hash)
print()

# Implementación de un algoritmo de consenso por prueba de trabajo
def proof_of_work(block, difficulty):
    target = "0" * difficulty
    nonce = 0
    while True:
        hash = hashlib.sha256((str(block.timestamp) + str(block.data) + str(block.previous_hash) + str(nonce)).encode()).hexdigest()
        if hash[:difficulty] == target:
            return nonce
        nonce += 1

block = Block("Hello World!", "0")
difficulty = 4
start_time = time.time()
nonce = proof_of_work(block, difficulty)
end_time = time.time()

print("Nonce: ", nonce)
print("Time: ", end_time - start_time, " seconds")
