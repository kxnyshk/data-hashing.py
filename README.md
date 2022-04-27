# data-hashing.py
A .py application to hash secure user entered sensitive data or passwords using the SHA3-256 Crypto Algorithm, to make one's available online data secure & resistive against possible data breaches online.

## Fetching the repo
 - Download the .zip file from [here](https://github.com/kxnyshk/data-hashing.py/archive/refs/heads/master.zip)
 - Unzip/Extract the directory.
 - Open the extracted directory in VsCode or any other IDE of your choice.

## How to execute
 - Open the Terminal of your choosen IDE.
 - Execute the [**main.py**](https://github.com/kxnyshk/data-hashing.py/blob/master/main.py) script, either by using the command:
    - `py main.py`        (Python execution) or
    - `nodemon main.py`   (Node/Nodemon execution)
    * (Make sure your system has Python/Node/Nodemon installed prior execution)

## Using the application
 - Enter your identity as asked   (official/non-offcial)
 - Enter the data/password you wanna hash
 - The SHA3-256 Hash (HexCode) for the specified data will be generated
 
 ### Commands
   - Press `-1`: to terminate the application.
   - Press `0`: to re-run **main.py**

## Hashing used
 - The hash algorithm used for hashing is **SHA3-256**
 - It belongs to the **SHA-3 Keccak** hash family
 - Based on the **Sponge construction** of cryptographic concept.
 - A version of SHA3-256, the **Keccak-256** is used in **Ethereum Blockchain** development.
 - The hash has been fetched via Python's **`hashlib`** library.

## Further Reads
 - [Secure Hash Algorithms | Cryptobook - Svetlin Nakov](https://cryptobook.nakov.com/cryptographic-hash-functions/secure-hash-algorithms)
 - [Password Hashing with Python | Medium - Felix Otoo](https://blog.devgenius.io/password-hashing-with-python-f3148692e8b9)
 - [SHA-3 Hash family | Wikipedia](https://en.wikipedia.org/wiki/SHA-3)
 - [Keccak Documentation | Keccak Team](https://keccak.team/specifications.html)
 - [The Sponge & Duplex constructions | Keccak Team](https://keccak.team/sponge_duplex.html)
 - [Ethereum's Cryptographic Hash fucntion | Oreilly.com](https://www.oreilly.com/library/view/mastering-ethereum/9781491971932/ch04.html#:~:text=Ethereum%E2%80%99s%20Cryptographic%20Hash%20Function%3A%20Keccak%2D256)
 - [hashlib Documentation | docs.python.org](https://docs.python.org/3/library/hashlib.html)
