num=[]

for i in range(1,4):
    file_name = input("enter a file name :")+".txt"
    file = open(file_name,'r')
    data = file.read()
    file.close()
      
    num.append(int(data))
print(num)

def find_prime(val):
    prime=True
    for i in range(2,val):
        if val%i==0:
            prime=False
    if prime:
        return True
    else :
        return False

for number in num:
    if find_prime(number) :
        prime=str(number)

file_name=input('enter create file name :')+".txt"
file = open(file_name,'x')
file.write(prime)
file.close()