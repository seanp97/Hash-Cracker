import hashlib
import sys

class Cracker:

    def __init__(self):   

        if sys.argv[1] != "":

            self.hash_choice = sys.argv[1]

            self.hash_check = input("Is your password hashed? (y/n): ")

            if self.hash_choice.lower() == "md5":
                if self.hash_check.lower() == "y":
                    self.Cracker_hashed_md5()
                elif self.hash_check.lower() == "n":
                    self.Cracker_unhashed_md5()

            elif self.hash_choice.lower() == "sha1":
                if self.hash_check.lower() == "y":
                    self.Cracker_hashed_sha1()
                elif self.hash_check.lower() == "n":
                    self.Cracker_unhashed_sha1()

            elif self.hash_choice.lower() == "sha256":
                if self.hash_check.lower() == "y":
                    self.Cracker_hashed_sha256()
                elif self.hash_check.lower() == "n":
                    self.Cracker_unhashed_sha256()
        else:

            print("Choose a hashing method")


    def Cracker_unhashed_md5(self):
        self.password_unhashed_md5 = input("Enter unhashed password: ")

        self.md5file_unhashed_md5 = open("rockyou.txt", "r", encoding="ISO-8859-1")

        self.exists_unhashed_md5 = False

        for x_unhashed_md5 in self.md5file_unhashed_md5:
            if x_unhashed_md5.strip() == self.password_unhashed_md5.strip():
                print("Match: " + hashlib.md5(x_unhashed_md5.strip().encode('utf-8')).hexdigest())
                self.exists_unhashed_md5 = True
                return

        if self.exists_unhashed_md5 == False:
            print("No match")



    def Cracker_hashed_md5(self):
        self.password_hashed_md5 = input("Enter hashed password: ")

        self.md5file_hashed_md5 = open("rockyou.txt", "r", encoding="ISO-8859-1")

        self.exists_hashed_md5 = False

        for x_hashed_md5 in self.md5file_hashed_md5:
            if hashlib.md5(x_hashed_md5.strip().encode('utf-8')).hexdigest() == self.password_hashed_md5.strip():
                print(f"Match {x_hashed_md5.strip()} :  {self.password_hashed_md5}")
                self.exists_hashed_md5 = True
                return

        if self.exists_hashed_md5 == False:
            print("No match")



    def Cracker_unhashed_sha1(self):
        self.password_unhashed_sha1 = input("Enter unhashed password: ")

        self.sha1file_unhashed_sha1 = open("rockyou.txt", "r", encoding="ISO-8859-1")

        self.exists_unhashed_sha1 = False

        for x_unhashed_sha1 in self.sha1file_unhashed_sha1:
            if x_unhashed_sha1.strip() == self.password_unhashed_sha1.strip():
                print("Match: " + hashlib.sha1(x_unhashed_sha1.strip().encode('utf-8')).hexdigest())
                self.exists_unhashed_sha1 = True
                return

        if self.exists_unhashed_sha1 == False:
            print("No match")


    def Cracker_hashed_sha1(self):
        self.password_hashed_sha1 = input("Enter hashed password: ")

        self.sha1file_hashed_sha1 = open("rockyou.txt", "r", encoding="ISO-8859-1")

        self.exists_hashed_sha1 = False


        for x_hashed_sha1 in self.sha1file_hashed_sha1:
            if hashlib.sha1(x_hashed_sha1.strip().encode('utf-8')).hexdigest() == self.password_hashed_sha1.strip():
                print(f"Match {x_hashed_sha1.strip()} :  {self.password_hashed_sha1}")
                self.exists_hashed_sha1 = True
                return

        if self.exists_hashed_sha1 == False:
            print("No match")


    def Cracker_unhashed_sha256(self):
        self.password_unhashed_sha256 = input("Enter unhashed password: ")

        self.sha256file_unhashed_sha256 = open("rockyou.txt", "r", encoding="ISO-8859-1")

        self.exists_unhashed_sha256 = False

        for x_unhashed_sha256 in self.sha256file_unhashed_sha256:
            if x_unhashed_sha256.strip() == self.password_unhashed_sha256.strip():
                print("Match: " + hashlib.sha256(x_unhashed_sha256.strip().encode('utf-8')).hexdigest())
                self.exists_unhashed_sha256 = True
                return

        if self.exists_unhashed_sha256 == False:
            print("No match")


    def Cracker_hashed_sha256(self):
        self.password_hashed_sha256 = input("Enter hashed password: ")

        self.sha256file_hashed_sha256 = open("rockyou.txt", "r", encoding="ISO-8859-1")

        self.exists_hashed_sha256 = False


        for x_hashed_sha256 in self.sha256file_hashed_sha256:
            if hashlib.sha256(x_hashed_sha256.strip().encode('utf-8')).hexdigest() == self.password_hashed_sha256.strip():
                print(f"Match {x_hashed_sha256.strip()} :  {self.password_hashed_sha256}")
                self.exists_hashed_sha256 = True
                return

        if self.exists_hashed_sha256 == False:
            print("No match")


Cracker()