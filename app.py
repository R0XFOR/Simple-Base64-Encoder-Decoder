from base64 import b64encode, b64decode
from sys import exit
from os import system

def mode():
	mode=str(input('(D)ecrypt or (E)ncrypt, or exit: '))
	if mode=='E':
		encrypt()
	if mode=='D':
		decrypt()
	if mode=='exit':
		exit()

def encrypt():
    str_msg=input('Enter message: ').encode('utf-8')
    base64msg_b=b64encode(str_msg)
    base64msg=base64msg_b.decode('utf-8')
    print(base64msg)
    mode()

	
def decrypt():
    base_message=input('Enter message: ').encode('utf-8')
    base_str=b64decode(base_message).decode('utf-8')
    print(base_str)
    mode()

system('cls||clear')
mode()