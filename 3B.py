from random import choice
charsets=['abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ',
          '1234567890','!@#$%^$^&*()_+']
def pswd(length=16):
    pwd=[]
    charset=choice(charsets)
    while len(pwd)<length:
        pwd.append(choice(charset))
        charset=choice(list(set(charsets)-set([charset])))
    return"".join(pwd)

print(pswd())
while True:
    c=1
    c=int(input("want a new password? enter 1 for yes and 0 for no"))
    if c==1:
        print(pswd())
    c=int(input("want a new password? enter 1 for yes and 0 for no"))
    if c==0:
        break
