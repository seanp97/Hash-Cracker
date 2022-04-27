Python Hash Cracker - By Sean Pelser

Make sure you have the rockyou.txt file in the same folder as the python file or you can use own as the third argument

Two arguments and one optional argument:
▼▼▼

{HashMethod} {hashed_password} {file_name} - Optional if you want to use own password list - if no argument, will default to rockyou.txt password list

----------------------------------------------------

At the terminal type "HashCracker.py {hash_method} {hashed_password} {file_name} - Optional"
▼▼▼

E.G "HashCracker.py sha224 631abe7d5d0cb4a7920b8f2c38ac89ea003673e3659aa28993adc8505711f878 {optional file_name}"

Which will crack 123456 as sha224


If the password is not in the file it will return no match
