import mysql.connector as sqltor 
def innput(r):
    for i in range(r):
                 nan=int(input('Enter the product id:'))
                 e=input('Enter the quantity of the product:')
                 f=input('Enter the Company Name:')
                 g=input('Enter the Model name:')
                 h=input('Enter the colour of the product:')
                 ii=input('Enter the Interanl Stroage the product:')
                 bb=input('Enter the battery life the product:')
                 rrr=input('Enter the RAM the product:')
                 mm=input('Enter the megapixel of camera of the product:')
                 ss=input('Enter the display type of the product:')
                 hh=input('Enter the warranty period of the product:')
                 ll=input('Enter the operating software of the product:')
                 j=input('Enter Date Of Manufacture the  of the product:')
                 k=input('Enter the date of New Stock Arrival of the product:')
                 l=input('Enter the Price of the product:')
                 m=input('Enter the  discounted Price of the product:')
                 n=input('Enter Service Status of the product:')
                 o=input('Enter the Service Charges of the product:')
                 re=str((nan,e,f,g,h,ii,bb,rrr,mm,ss,hh,j,ll,l,m))
                 se=str((nan,e,f,g,hh,j,k,l,m,n,o))
                 db.execute('insert into mobile_information values'+re)
                 db.execute('insert into mobile_sales values'+se)
                 mycon.commit()
    return 
####################################################################################################################                 
def ppirt(ff,wa,ta):
    for nn in ff:
        if (nn[1]==wa and nn[2]==ta):
            dof=str(nn[5])
            qqp=dof.lstrip('datetime.date')
            qsp=str(nn[0])
            print('''|----------------------------------------------|\n'''
                  '''|product ID:'''+qsp+'''                        \n'''
                  '''|company:'''+nn[1]+'''                         \n'''
                  '''|model name:'''+nn[2]+'''                      \n'''
                  '''|Service Status:'''+nn[3]+'''                  \n'''
                  '''|Service Charges:'''+nn[4]+'''                 \n'''
                  '''|Date Of Manufacture:'''+qqp+'''               \n'''
                  '''|Warranty_period:'''+nn[6]+'''                 \n'''
                  '''|----------------------------------------------|''')
    return           
####################################################################################################################   
def pprt(fff,jh,jt):
    for nn in fff:
        if (nn[2]==jh and nn[3]==jt):
            we=str(nn[11])
            qqp=we.lstrip('datetime.date')
            qsp=str(nn[0])
            print('''|----------------------------------------------| \n'''
                  '''|product ID:'''+qsp+'''                          \n'''
                  '''|quantaty:'''+nn[1]+'''                          \n'''
                  '''|company:'''+nn[2]+'''                           \n'''
                  '''|model name:'''+nn[3]+'''                        \n'''
                  '''|colour:'''+nn[4]+'''                            \n'''
                  '''|internal stroage:'''+nn[5]+'''                  \n'''
                  '''|battery life:'''+nn[6]+'''                      \n'''
                  '''|RAM:'''+nn[7]+'''                               \n'''
                  '''|camera megapixel:'''+nn[8]+'''                  \n'''
                  '''|Display type:'''+nn[9]+'''                      \n'''
                  '''|warranty period:'''+nn[10]+'''                  \n'''
                  '''|date of manufacture:'''+qqp+'''                 \n'''
                  '''|operating software:'''+nn[12]+'''               \n'''
                  '''|price:'''+nn[13]+'''                            \n'''
                  '''|dicounted price:'''+nn[14]+'''                  \n'''
                  '''|----------------------------------------------|''')
    return
####################################################################################################################   
def ppt(ffff,we,wr):
     for nn in ffff:
         if (nn[2]==we and nn[3]==wr):
            we=str(nn[5])
            qqp=we.lstrip('datetime.date')
            ws=str(nn[6])
            aqw=ws.lstrip('datetime.date')
            qsp=str(nn[0])
            print('''|----------------------------------------------|\n'''
                  '''|product ID:'''+qsp+'''                         \n'''
                  '''|quantaty:'''+nn[1]+'''                         \n'''
                  '''|company:'''+nn[2]+'''                          \n'''
                  '''|model name:'''+nn[3]+'''                       \n'''
                  '''|warranty period:'''+nn[4]+'''                  \n'''
                  '''|date of manufacture:'''+qqp+'''                \n'''
                  '''|New Stock Arrival:'''+aqw+'''                  \n'''
                  '''|price:'''+nn[7]+'''                            \n'''
                  '''|dicounted price:'''+nn[8]+'''                  \n'''
                  '''|Service_Status:'''+nn[9]+'''                   \n'''
                  '''|Service_Charges:'''+nn[10]+'''                 \n'''
                  '''|----------------------------------------------|''')  
     return
####################################################################################################################  
mycon=sqltor.connect(host='localhost',user='root',database='school')
db=mycon.cursor()
if mycon.is_connected():
        print("Database connected successfully....")
else:
        print("Server not connected...!")
 
a=1
while a<5:
    print('----------MENU---------')
    print('Enter 1 for user admin:')
    print('Enter 2 for service of your device:')
    print('Enter 3 for information regrading the products:')
    print('Enter 4 for infromation relate to the seller:')
    print('Enter 5 to Exit:')
    a=int(input('Enter the respective number from above:'))
    if a==1:
        print('----------MENU---------')
        print('Enter 1 if table not created:')
        print('Enter 2 if table is created:')
        c=int(input('Enter the respective number from above:'))
        print('----------MENU---------')
        print('Enter 1 for mobiles informaton interface:')
        print('Enter 2 for modifying the table:')
        b=int(input('Enter the respective number from above:'))
#####################################################################################################################################
        if b==1:
           if c==1:
                db.execute('create table mobile_information (PID int PRIMARY KEY,QTY varchar(20),Company_Name varchar(30),Model_Name varchar(20),Colour varchar(20),Memory varchar(20),Battery_file varchar(20),RAM varchar(20),Camera_megapixel varchar(20),Display_Type varchar(20),Warranty_period varchar(20),D_O_M  date,OS varchar(20),Price varchar(20),DISCOUNT_PRICE varchar(20))')
                db.execute('create table mobile_sales (PID int PRIMARY KEY,QTY varchar(20),Company_Name varchar(30),Model_Name varchar(20),Warranty_period varchar(20),Date_Of_Manufacture date,New_Stock_Arrival date,Price varchar(20),Dicounted_Price varchar(20),Service_Status varchar(20),Service_Charges varchar(20))')
                d=int(input('Enter how many inputs you want in the table:'))
                innput(d)
           else:
                 d=int(input('Enter how many inputs you want in the table:'))
                 innput(d)
                 print('----------MENU---------')
                 print('Enter 1 to print the input:')
                 print('Enter 2 to continue:')
                 a=int(input('Enter the respective number from above:'))
                 if a==1:
                     db.execute("select * from mobile_information")
                     pprt(db)
                     db.execute("select * from mobile_sales")
                     ppt(db)
                 else:
                     pass
      
        if b==2:
            print('----------MENU---------')
            print('Enter 1 for delete a row from the table:')
            print('Enter 2 for changing the value in a prticular row:')
            ai=int(input('Enter the respective number from above:'))
           
            if ai==1:
                r=input('enter the product id of the product whose values to be deleted')
                db.execute('delete from  mobile_information where PID="'+r+'"')
                db.execute('delete from  mobile_sales where PID="'+r+'"')
                mycon.commit()
            if ai==2:
                f=input('enter the exact name of the coloum whose vaule you you want to change:')
                b=input('enter the new value you want')
                h=input('Enter the product id')
                db.execute('update mobile_information set '+f+'="'+b+'" where PID="'+h+'"')
                db.execute('update mobile_sales set '+f+'="'+b+'" where PID="'+h+'"')
                mycon.commit()
            
#####################################################################################################################################
    if a==2:
            db.execute("select PID ,company_Name,Model_Name,Service_Status,Service_Charges,Date_Of_Manufacture,Warranty_period from mobile_sales")
            nix=input('Enter the name of the company:')
            wix=input('Enter the model name:')
            ppirt(db,nix,wix)
        
#####################################################################################################################################
    if a==3:
            db.execute("select * from mobile_information")
            qw=input('Enter the name of the company:')
            qa=input('Enter the model name:')
            pprt(db,qw,qa)
       
#####################################################################################################################################
    if a==4:
            db.execute("select * from mobile_sales")
            qr=input('Enter the name of the company:')
            qi=input('Enter the model name:')
            ppt(db,qr,qi)
        
#####################################################################################################################################
print('Thank you')      
      