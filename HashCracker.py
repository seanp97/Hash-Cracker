import hashlib
import sys

class Cracker:

    def __init__(self):   

        if len(sys.argv) > 1:

            print("  ___ ___               .__    _________                       __                 ")
            print(" /   |   \_____    _____|  |__ \_   ___ \____________    ____ |  | __ ___________") 
            print("/    ~    \__  \  /  ___/  |  \/    \  \/\_  __ \__  \ _/ ___\|  |/ // __ \_  __ \\")
            print("\    Y    // __ \_\___ \|   Y  \     \____|  | \// __ \\  \___|    <\  ___/|  | \/")
            print(" \___|_  /(____  /____  >___|  /\______  /|__|  (____  /\___  >__|_ \\___  >__|   ")
            print("       \/      \/     \/     \/        \/            \/     \/     \/    \/       ")

            print("")
            print("")

            self.hash_choice = sys.argv[1]

            self.hashed_password = sys.argv[2]

            self.password_list = ""
            if len(sys.argv) > 3:
                print(sys.argv[3])
            else:
                self.password_list = "rockyou.txt"

            if self.hash_choice.lower() == "md5":
                self.Cracker_hashed_md5()

            elif self.hash_choice.lower() == "sha1":
                self.Cracker_hashed_sha1()

            elif self.hash_choice.lower() == "sha224":
                self.Cracker_hashed_sha224()

            elif self.hash_choice.lower() == "sha256":
                self.Cracker_hashed_sha256()

            elif self.hash_choice.lower() == "sha512":
                self.Cracker_hashed_sha512()

            elif self.hash_choice.lower() == "blake2b":
                self.Cracker_hashed_blake2b()

            elif self.hash_choice.lower() == "blake2s":
                self.Cracker_hashed_blake2s()

            else:
                print("Not a valid hash method")

        else:
            print("Choose a hashing method")



    def Cracker_hashed_md5(self):
        print("Cracking...")
        print("")
        self.md5file_hashed_md5 = open(f"{self.password_list}", "r", encoding="ISO-8859-1")
        self.exists_hashed_md5 = False

        for x_hashed_md5 in self.md5file_hashed_md5:
            if hashlib.md5(x_hashed_md5.strip().encode('utf-8')).hexdigest() == self.hashed_password.strip():
                print(f"MATCH  -  {x_hashed_md5.strip()}  :  {self.hashed_password}")
                print("")
                print("▼▼▼")
                self.exists_hashed_md5 = True
                return

        if self.exists_hashed_md5 == False:
            print("No match")



    def Cracker_hashed_sha1(self):
        print("Cracking...")
        print("")
        self.sha1file_hashed_sha1 = open(f"{self.password_list}", "r", encoding="ISO-8859-1")
        self.exists_hashed_sha1 = False

        for x_hashed_sha1 in self.sha1file_hashed_sha1:
            if hashlib.sha1(x_hashed_sha1.strip().encode('utf-8')).hexdigest() == self.hashed_password.strip():
                print(f"MATCH  -  {x_hashed_sha1.strip()}")
                print("")
                print("▼▼▼")
                print(self.hashed_password)
                self.exists_hashed_sha1 = True
                return

        if self.exists_hashed_sha1 == False:
            print("No MATCH")


    def Cracker_hashed_sha224(self):
        print("Cracking...")
        print("")
        self.sha224file_hashed_224 = open(f"{self.password_list}", "r", encoding="ISO-8859-1")
        self.exists_hashed_sha224 = False

        for x_hashed_sha224 in self.sha224file_hashed_224:
            if hashlib.sha224(x_hashed_sha224.strip().encode('utf-8')).hexdigest() == self.hashed_password.strip():
                print(f"MATCH  -  {x_hashed_sha224.strip()}")
                print("")
                print("▼▼▼")
                print(self.hashed_password)
                self.exists_hashed_shav = True
                return

        if self.exists_hashed_sha224 == False:
            print("No MATCH")



    def Cracker_hashed_sha256(self):
        print("Cracking...")
        print("")
        self.sha256file_hashed_sha256 = open(f"{self.password_list}", "r", encoding="ISO-8859-1")
        self.exists_hashed_sha256 = False

        for x_hashed_sha256 in self.sha256file_hashed_sha256:
            if hashlib.sha256(x_hashed_sha256.strip().encode('utf-8')).hexdigest() == self.hashed_password.strip():
                print(f"MATCH  -  {x_hashed_sha256.strip()}")
                print("")
                print("▼▼▼")
                print(self.hashed_password)
                self.exists_hashed_sha256 = True
                return

        if self.exists_hashed_sha256 == False:
            print("No match")



    def Cracker_hashed_sha512(self):
        print("Cracking...")
        print("")
        self.sha512file_hashed_sha512 = open(f"{self.password_list}", "r", encoding="ISO-8859-1")
        self.exists_hashed_sha512 = False

        for x_hashed_sha512 in self.sha512file_hashed_sha512:
            if hashlib.sha512(x_hashed_sha512.strip().encode('utf-8')).hexdigest() == self.hashed_password.strip():
                print(f"MATCH  -  {x_hashed_sha512.strip()}")
                print("")
                print("▼▼▼")
                print(self.hashed_password)
                self.exists_hashed_sha512 = True
                return

        if self.exists_hashed_sha512 == False:
            print("No match")


    def Cracker_hashed_blake2b(self):
        print("Cracking...")
        print("")
        self.blake2bfile_hashed_blake2b = open(f"{self.password_list}", "r", encoding="ISO-8859-1")
        self.exists_hashed_blake2b = False

        for x_hashed_blake2b in self.blake2bfile_hashed_blake2b:
            if hashlib.blake2b(x_hashed_blake2b.strip().encode('utf-8')).hexdigest() == self.hashed_password.strip():
                print(f"MATCH  -  {x_hashed_blake2b.strip()}")
                print("")
                print("▼▼▼")
                print(self.hashed_password)
                self.exists_hashed_blake2b = True
                return

        if self.exists_hashed_blake2b == False:
            print("No match")


    def Cracker_hashed_blake2s(self):
        print("Cracking...")
        print("")
        self.blake2sfile_hashed_blake2s = open(f"{self.password_list}", "r", encoding="ISO-8859-1")
        self.exists_hashed_blake2s = False

        for x_hashed_blake2s in self.blake2sfile_hashed_blake2s:
            if hashlib.blake2s(x_hashed_blake2s.strip().encode('utf-8')).hexdigest() == self.hashed_password.strip():
                print(f"MATCH  -  {x_hashed_blake2s.strip()}")
                print("")
                print("▼▼▼")
                print(self.hashed_password)
                self.exists_hashed_blake2s = True
                return

        if self.exists_hashed_blake2s == False:
            print("No match")


Cracker()
