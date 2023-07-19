#libraries for AES encryptio
from  Cryptodome.Cipher import AES
from Crypto.Util.Padding import pad
#libraries for RSA encryption
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
#libraries for BLOWFISH  encryption
from Cryptodome.Cipher import Blowfish
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad
#libraries for ECC encryption
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

