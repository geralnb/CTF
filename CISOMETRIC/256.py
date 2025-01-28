import hashlib
import requests
import re


CHALLENGE_URL = "http://103.127.97.242:31337/"
VALIDATE_URL = "http://103.127.97.242:31337/validate.php"

def solve_challenge():
    with requests.Session() as session:
        
        response = session.get(CHALLENGE_URL, timeout=2)
        if response.status_code != 200:
            print("Gagal mengambil halaman challenge.")
            return

        
        match = re.search(r'id="random-string".*?>(.*?)<', response.text)
        if not match:
            print("Gagal menemukan random string.")
            return

        random_string = match.group(1).strip()
        print(f"Random String: {random_string}")

        
        hash_object = hashlib.sha256(random_string.encode())
        sha256_hash = hash_object.hexdigest()
        print(f"SHA-256 Hash: {sha256_hash}")

        
        data = {
            "random_string": random_string,
            "hash": sha256_hash,
        }

        response = session.post(VALIDATE_URL, data=data, timeout=2)
        if response.status_code == 200:
            print("Response dari server:")
            print(response.text)
        else:
            print(f"Request gagal dengan status code {response.status_code}")

if __name__ == "__main__":
    solve_challenge()
