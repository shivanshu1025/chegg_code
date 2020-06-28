#1. Dictionary: You need to build two main dictionaries before the user menu:
#a) a key for the book ISBN number, value is a list of book’s title and price.
#b) a key of the name of the book, value is a list of ISBN number and price.

dic1={"ISBN1":["BOOK1",1000],"ISBN2":["BOOK2",2000]}
dic2={"BOOK1":["ISBN1",1000],"BOOK2":["ISBN2",2000]}
total=[]
sum=0
ISBN="0"
def checkout():
    sum=0
    for x in total:
        sum=sum+x
    print("Your Total Amount is ",sum)
    

while(1):
    choice=input("Do You Want To Shop (y/n) : ")
    if choice=="y":
          option=int(input(""" PLEASE SELECT THE OPTION(1,2,3,4)
           1. Purchase by ISBN:
           2. Purchase by Title:)
           3. Checkout:
           4. Quit Application:\n"""))
          if option==1:
             ISBN=input("ENTER THE ISBN(International Standard Book Number): ")
             if ISBN in dic1:
                print("BOOK TITLE: ",dic1[ISBN][0])
                print("BOOK PRICE: ",dic1[ISBN][1])
                buy=input("Do You Want To Purchase This Book y/n ")
                if buy=='y':
                   total.append(dic1[ISBN][1])
                   print("Added To Cart Successfully ")
                
                else:
                    checkout()
                    break
             else:
               print("ISBN Doesn't Match ")
          elif option==2:
              TITLE=input("ENTER THE TITLE OF BOOK : ")
              if TITLE in dic2:
                print("BOOK ISBN: ",dic2[TITLE][0])
                print("BOOK PRICE: ",dic2[TITLE][1])
                buy=input("Do You Want To Purchase THIS BOOK y/n ")
                if buy=='y':
                   total.append(dic2[TITLE][1])
                   print("Added To Cart Successfully ")
                
                else:
                    checkout()
                    print("THANKS FOR VISITING")
                    break
              else:
                print("BOOK TITLE Doesn't Match ")

            
          elif option==3:
              checkout()
              break
          elif option==4:
              checkout()
              exit(0)
    else:
        if len(total)==0:
            print("THANKU FOR VISITING ")
            break
        else:
            checkout()
            break
      


