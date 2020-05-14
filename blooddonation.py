#python code to make or udate data of user for blood donation
#hackathon 1
#Team Member : PRIYAM (19BCS089) and SATYAM KUMAR (19BEC040)
import sys
import csv
donor=[]
reciepient=[]    
while True:
    
    
        print('\n1. Enter Donor data\n2. Enter Recipient data\n3. Get Donor data\n4. Get Recipient data\n5. Exit From The system')
        ch = int(input('\nEnter your choice :'))
        if ch==1:
            print('\nEnter the following details of the Person:')
            Name=input("Donor name:")
            usid=input("\nUser id:")
            pno=input("\nPhone Number:")
            Email=input("\nEmail id:")
            Addr=input("\nAddress:")
            bg=input("\nBloodGroup")
            Age=int(input("\nAge:"))
            with open('blooddonor.csv','a',newline='') as f:
               
               thewriter=csv.writer(f)
               thewriter.writerow([usid,Name,pno,Email,Addr,bg,Age])
               f.close()
            print("\n\nThank You!!New Donor Registered")
        elif ch==2:
            print("\nEnter following details:")
            Rpid=input('\nReciepient ID:')
            Name=input("Reciepient Name:")
            Sex=input("Gender:")
            Bg=input("BloodGroup:")
            HName=input("Hospital Name:")
            with open('reciepient.csv','a',newline='') as R:
                writ=csv.writer(R)
                writ.writerow([Rpid,Name,Sex,Bg,HName])
                R.close()
            print("\n\nDetails recieved!")
        elif ch==3:
             with open('blooddonor.csv','r') as f:
                 reader=csv.reader(f)
                 for row in reader:
                     donor.append(row)
             usid=input('\nDonor id:')
             col=[x[0]for x in donor]
             if usid in col:
                 for x in range(0,len(donor)):
                     if usid==donor[x][0]:
                         print(donor[x])
            
             else:
                 print("\nInvalid Donor ID!!")
             f.close()
            
        elif ch==4:
            with open('reciepient.csv','r') as R:
                reader=csv.reader(R)
                for row in reader:
                    reciepient.append(row)
            Rid=input('\nReciepient ID:')
            col=[x[0]for x in reciepient]
            if Rid in col:
                for x in range(0,len(reciepient)):
                    if Rid==reciepient[x][0]:
                        print(reciepient[x])
            else:
                print('\nInvalid ID')
            R.close()
        elif ch==5:
            print('\n\nThank you for using our system!!!!\n\n')
            sys.exit()
        else:
            print("\n\nSorry Wrong Option!!\n We Regret For This Inconvenience Caused!!\n----Try Again!!----")