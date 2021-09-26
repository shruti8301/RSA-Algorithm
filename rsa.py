import math
import timeit
def gcd(a, h):
    while(1):
        temp=a%h
        if(temp==0):
            return h
        a=h
        h=temp
def rsa(msg):
    p=7
    q=11
    n=p*q
    e=13
    phi=(p-1)*(q-1)
    while(e<phi):
        if(gcd(e,phi)==1):
            break
        else:
            e+=1
    k=1       
    while(True):
         d = (1 + (k*phi))/e
         if(round(d,5)%1==0):
             break  
         else:
             k+=1
    
    numbers = []
    for letter in msg:
        if(letter==" "):
            numbers.append(-1)
        else:
            number = ord(letter) - 96
            numbers.append(number-1)
    t = timeit.timeit(lambda: enc(numbers,e,n,d),number=1)
    print("Encryption Response Time: " , t)
   

def enc(numbers,e,n,d):
    #encryption  c = (msg ^ e) % n
    encp=[]
    for i in range(len(numbers)):
        #if(numbers[i]==-1):
            #encp.append(-1)
        #else:
            c=(numbers[i]**e) % n
            g=c % n
            encp.append(g)
    res = " ".join([chr(i) for i in encp])
    print("Encrypted Message: " , str(res))
    dt = timeit.timeit(lambda: decryption(encp,d,n),number=1)
    print("Decryption Response Time: " , dt)
    

def decryption(encp,d,n):
    #Decryption m = (c ^ d) % n
    denc=[]
    
    for i in range(len(encp)):
        if(encp[i]==-1):
            denc.append(chr(32))
        else:
            m=(encp[i]**int(d))%n
            h=m%n

        denc.append(chr(h+97))
    resd = " ".join([str(i) for i in denc])
    print("Decrypted Message: " , str(resd))

msg=input()
print("Message: ", msg )
rt = timeit.timeit(lambda: rsa(msg),number=1)
print("RSA Function Time: ", rt)
    

