import rsa

def main():
    public_key, private_key = rsa.newkeys(1024)

    message = b"I like sushi"

    cipher_text = rsa.encrypt(message, public_key)

    decrypted_message = rsa.decrypt(cipher_text, private_key)

    signature = rsa.sign(message, private_key, 'SHA-1')

    try:
        rsa.verify(message, signature, public_key)
        verified = True
    except rsa.VerificationError:
        verified = False

    print("Original Message: ", message)
    print("Encrypted Message: ", cipher_text)
    print("Decrypted Message: ", decrypted_message)
    print("Signature: ", signature)
    print("Verification: ", verified)



if __name__ == "__main__":
    main()
