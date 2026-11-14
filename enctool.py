#!/usr/bin/env python3
# EncTool - Encrypt/Decrypt Bash & Encrypt Python (Marshal)
# Original Copyright (c) 2023 cheos969
# Licensed under MIT License
# Modified for Python 3 / Termux compatibility

import os, sys, time, marshal

os.system('clear' if os.name != 'nt' else 'cls')

logo = """\a\a\33[32m
 ███████╗ ███╗   ██╗  ██████╗ ██████╗  ██╗   ██╗ ██████╗  ████████╗
 ██╔════╝ ████╗  ██║ ██╔════╝ ██╔══██╗ ╚██╗ ██╔╝ ██╔══██╗ ╚══██╔══╝
 █████╗   ██╔██╗ ██║ ██║      ██████╔╝  ╚████╔╝  ██████╔╝    ██║
 ██╔══╝   ██║╚██╗██║ ██║      ██╔══██╗   ╚██╔╝   ██╔═══╝     ██║
 ███████╗ ██║ ╚████║ ╚██████╗ ██║  ██║    ██║    ██║         ██║
 ╚══════╝ ╚═╝  ╚═══╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝    ╚═╝         ╚═╝
\33[0;1m           Protect your code and copyright by encrypting
               them using this encrypter script
\33[34m________________________________________________________________________
 \33[31;1m          Author : Cheos | YouTube : Cheos969 \33[36;1m

1- Encrypt Bash
2- Decrypt Bash
3- Encrypt Python Marshal
4- About
0- Exit
\33[0m"""

about = """\33[32;1m
coded by Cheos969

YouTube Cheos969

This script is written in python, you can use
this script to encrypt/decrypt your bash scripts
and you can also encrypt python code in marshal
just type enctool to run this script

follow developer»»————>
Youtube   : Cheos969
TikTok     : Chs969
\33[0m"""


def encbash():
    in_file = input("Input filename: ").strip()
    if not os.path.exists(in_file):
        print("error, file not found")
        return encbash()
    if os.system("bash-obfuscate " + in_file + " -o .temp") != 0:
        print("error, gagal obfuscate. Pastikan bash-obfuscate terinstall.")
        return
    out_file = input("Output Filename: ").strip()
    if not out_file:
        out_file = in_file.replace(".sh", "") + "_enc.sh"
    try:
        with open(".temp", "r") as temp_f, open(out_file, "w") as out_f:
            encdata = temp_f.read()
            out_f.write("# Encrypted by Cheos969\n"
                        "# Saluran : https://whatsapp.com/channel/0029VbDOPkQKmCPRWoRAJE0m\n\n"
                        + encdata)
        os.remove(".temp")
        print("successfully encrypted " + in_file + " and saved as " + out_file)
    except Exception as e:
        print("error: " + str(e))
        if os.path.exists(".temp"):
            os.remove(".temp")


def decbash():
    in_file = input("Input Filename: ").strip()
    if not os.path.exists(in_file):
        print("error, file not found")
        return decbash()
    with open(in_file, "r") as in_f:
        filedata = in_f.read()
    if "eval" not in filedata:
        print("error, file tidak bisa didekripsi (tidak ada 'eval')")
        return
    newdata = filedata.replace("eval", "echo", 1)
    with open(".temp1", "w") as temp_f:
        temp_f.write(newdata)
    out_file = input("Output filename: ").strip()
    if not out_file:
        out_file = in_file.replace(".sh", "") + "_dec.sh"
    os.system("bash .temp1 > .temp2")
    os.remove(".temp1")
    with open(".temp2", "r") as temp_f2, open(out_file, "w") as out_f:
        filedata = temp_f2.read()
        out_f.write("# Decrypted by Cheos969\n"
                    "# Saluran : https://whatsapp.com/channel/0029VbDOPkQKmCPRWoRAJE0m\n\n"
                    + filedata)
    os.remove(".temp2")
    print("successfully decrypted " + in_file + " and saved as " + out_file)


def encpy():
    try:
        file = input("Enter the file name: ").strip()
    except KeyboardInterrupt:
        sys.exit()
    if not os.path.exists(file):
        print("No such file")
        sys.exit()
    As = file.replace(".py", "")
    try:
        with open(file, "r") as f:
            strng = f.read()
        code = compile(strng, file, "exec")
        data = marshal.dumps(code)
    except SyntaxError as e:
        print("SyntaxError: " + str(e))
        sys.exit()
    except Exception as e:
        print("Error: " + str(e))
        sys.exit()

    with open(As + "_en.py", "w") as fileout:
        fileout.write("# Encrypted by Cheos969\n")
        fileout.write("# Original: https://github.com/Anon4You/EncTool\n")
        fileout.write("import marshal\n")
        fileout.write("exec(marshal.loads(" + repr(data) + "))")
    time.sleep(1)
    print("The name of the new encrypted file: " + As + "_en.py")


def main():
    print(logo)
    choice = input("Your Choice: ").strip()
    if choice == "1":
        encbash()
    elif choice == "2":
        decbash()
    elif choice == "3":
        encpy()
    elif choice == "4":
        print(about)
    elif choice == "0":
        print("thanks for using this script")
        time.sleep(1)
        sys.exit()
    else:
        print("Wrong input please try again..")
        time.sleep(2)
        main()


if __name__ == "__main__":
    main()