import random
import math


# Step 1: Generate two different prime numbers p and q
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if num % 2 != 0 and is_prime(num):
            return num


def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Miller-Rabin primality test
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# Step 2: Calculate N = p * q
def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    return (n, p, q)


# Step 3: Choose a public exponent e
def choose_public_exponent(phi):
    while True:
        e = random.randint(2, phi - 1)
        if math.gcd(e, phi) == 1:
            return e


# Step 4: Calculate private exponent d
def calculate_private_exponent(e, phi):
    return pow(e, -1, phi)



# Step 5: Encrypt a simple message using the public key
def encrypt(message, public_key):
    n, e = public_key
    encoded_msg = message.encode('utf-8')
    encrypted_msg = [pow(byte, e, n) for byte in encoded_msg]
    return encrypted_msg


# Step 6: Decrypt the message using the private key
def decrypt(encrypted_msg, private_key):
    n, d = private_key
    decrypted_bytes = [pow(byte, d, n) for byte in encrypted_msg]
    decrypted_msg = bytes(decrypted_bytes).decode('utf-8')
    return decrypted_msg


# Main program
bits = 1024
n, p, q = generate_keypair(bits)
phi = (p - 1) * (q - 1)
e = choose_public_exponent(phi)
d = calculate_private_exponent(e, phi)

public_key = (n, e)
private_key = (n, d)

message = "sushi!"
encrypted_msg = encrypt(message, public_key)
print("Encrypted message:", encrypted_msg)

decrypted_msg = decrypt(encrypted_msg, private_key)
print("Decrypted message:", decrypted_msg)
