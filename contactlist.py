import pymysql


db = pymysql.connect(host="localhost",
                     user="root",
                     password='',
                     port=3307,
                     database="contact")

cur=db.cursor()


class contact_list:

    def contact_info():
        while True:
            print('''enter the choice:
                   1.View all the details of the contact
                   2.search contact by name.
                   3.add contact details
                   4.delete a contact
                   ''')
            choice=int(input("enter the choice "))
            if choice == 1:
                  selectquery="select * from contact_book"
                  cur.execute(selectquery)
                  result=cur.fetchall()
                  #print(result)
                  for a in result:
                      b=(f'{a[0]}\t{a[1]}\t{a[2]}\t{a[3]}')
                      print(b)
            elif choice == 2:
                name=input("enter the name")
                selectquery=f'select * from contact_book where name="{name}"'
                cur.execute(selectquery)
                result=cur.fetchone()
                print(result)
            elif choice == 3:
                name=input("enter the name you want to update ")
                phone_num=int(input("enter the new phone number "))
                updatequery=f'UPDATE contact_book SET phone_num={phone_num} where name="{name}" '
                cur.execute(updatequery)
                db.commit()
            elif choice == 4:
                name=input("enter the name ")
                deletequery=f'delete from contact_book where name="{name}"'
                cur.execute(deletequery)
                db.commit
            else:
                print("enter correct option")
a=contact_list
a.contact_info()
                
                
                  
        
