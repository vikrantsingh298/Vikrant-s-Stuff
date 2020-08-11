def printtri(n,c):


   for i in range(1,n+1):

      if bool(c)==True:
        print("*"*i)

      else:
        print("*"*(n+1-i))  

   


printtri(int(input()),bool(int(input())))