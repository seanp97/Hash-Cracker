import hashlib
import sys

class Cracker:

    def __init__(self):   

        if sys.argv[1] != "":

            self.hash_choice = sys.argv[1]

            self.hashed_password = sys.argv[2]

            if self.hash_choice.lower() == "md5":
                self.Cracker_hashed_md5()

            elif self.hash_choice.lower() == "sha1":
                self.Cracker_hashed_sha1()

            elif self.hash_choice.lower() == "sha256":
                self.Cracker_hashed_sha256()

            elif self.hash_choice.lower() == "sha512":
                self.Cracker_hashed_sha512()

            else:
                print("Not a valid hash method")

        else:
            print("Choose a hashing method")



    def Cracker_hashed_md5(self):
        self.md5file_hashed_md5 = open("rockyou.txt", "r", encoding="ISO-8859-1")
        self.exists_hashed_md5 = False

        for x_hashed_md5 in self.md5file_hashed_md5:
            if hashlib.md5(x_hashed_md5.strip().encode('utf-8')).hexdigest() == self.hashed_password.strip():
                print(f"Match {x_hashed_md5.strip()} :  {self.hashed_password}")
                self.exists_hashed_md5 = True
                return

        if self.exists_hashed_md5 == False:
            print("No match")



    def Cracker_hashed_sha1(self):
        self.sha1file_hashed_sha1 = open("rockyou.txt", "r", encoding="ISO-8859-1")
        self.exists_hashed_sha1 = False

        for x_hashed_sha1 in self.sha1file_hashed_sha1:
            if hashlib.sha1(x_hashed_sha1.strip().encode('utf-8')).hexdigest() == self.hashed_password.strip():
                print(f"Match {x_hashed_sha1.strip()} :  {self.hashed_password}")
                self.exists_hashed_sha1 = True
                return

        if self.exists_hashed_sha1 == False:
            print("No match")



    def Cracker_hashed_sha256(self):
        self.sha256file_hashed_sha256 = open("rockyou.txt", "r", encoding="ISO-8859-1")
        self.exists_hashed_sha256 = False

        for x_hashed_sha256 in self.sha256file_hashed_sha256:
            if hashlib.sha256(x_hashed_sha256.strip().encode('utf-8')).hexdigest() == self.hashed_password.strip():
                print(f"Match {x_hashed_sha256.strip()} :  {self.hashed_password}")
                self.exists_hashed_sha256 = True
                return

        if self.exists_hashed_sha256 == False:
            print("No match")



    def Cracker_hashed_sha512(self):
        self.sha512file_hashed_sha512 = open("rockyou.txt", "r", encoding="ISO-8859-1")
        self.exists_hashed_sha512 = False

        for x_hashed_sha512 in self.sha512file_hashed_sha512:
            if hashlib.sha512(x_hashed_sha512.strip().encode('utf-8')).hexdigest() == self.hashed_password.strip():
                print(f"Match {x_hashed_sha512.strip()} :  {self.hashed_password}")
                self.exists_hashed_sha512 = True
                return

        if self.exists_hashed_sha512 == False:
            print("No match")


Cracker()
