import mysql.connector

def conn1():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'project'
    )

class db:
    def get(self, user):
        try:
            if user == 'student':
                query1 = "select * from student"
            conn = conn1()
            self.cursor = conn.cursor(buffered=True , dictionary=True)
            self.cursor.execute(query1)
            result = self.cursor.fetchall()
            return result
        except:
            return None

    def login(self,value):
        try:
            query1 = 'select * from student where student_email = %s'
            query2 = 'select * from tutor where tutor_email = %s'
            query3 = 'select * from staff where staff_email = %s'

            conn = conn1()
            cursor = conn.cursor(buffered=True , dictionary=True)

            cursor.execute(query1,value)
            result1 = cursor.fetchone()

            cursor.execute(query2,value)
            result2 = cursor.fetchone()
            
            cursor.execute(query3,value)
            result3 = cursor.fetchone()

            conn.close()
            cursor.close()
            if result1:
                result1.update({'role':'student'})
                return result1
            elif result2:
                result2.update({'role':'tutor'})
                return result2
            elif result3:
                result3.update({'role':'staff'})
                return result3
            else:
                return None

        except:
            raise Exception
            return None
    
    def signup(self,user,value):
        try:
            query1 = "insert into student(student_email,student_password,student_name) values(%s,%s,%s)"
            query2 = "insert into staff(staff_email,staff_password,staff_name) values(%s,%s,%s)"
            query3 = "insert into tutor(tutor_email,tutor_password,tutor_name) values(%s,%s,%s)"
            conn =conn1()
            print(user)
            cursor = conn.cursor(buffered=True, dictionary=True)
            if ( user == 'student'):
                cursor.execute(query1,value)
            elif( user == 'tutor'):
                cursor.execute(query3,value)
            elif( user == 'staff'):
                print('here')
                cursor.execute(query2,value)
            conn.commit()
            row_affected = cursor.rowcount
            conn.close()
            cursor.close()
            return row_affected
        except:
           # raise Exception
            return
            
