file=open("email.txt", 'w')
switch=True
print ("Type exit to exit")
while switch==True:
    email=input("Your Email: ")
    if email=="exit":
        switch=False
    elif email== "":
        pass
    else:
        file.write(email)
        file.write('\n')
file.close
print ("Done")





