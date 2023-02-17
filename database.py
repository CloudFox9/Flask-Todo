import sqlite3
from constants import errorFunction as erfc

""" Table Format - 
 CREATE TABLE "todolist" (
    "id" NUMBER NOT NULL,
    "item" TEXT NOT NULL,
    "status" TEXT NOT NULL,
    PRIMARY KEY("id")
);
"""

#database path
DB_PATH = './todo.db' 


#create uniue id (max +1)
def generate_id():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        return list(c.execute("select MAX(id) from todolist;"))[0][0] + 1

#addition of new task in database        
def addTask(task):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            id = generate_id()
            c.execute('insert into todolist(id,item,status) values(?,?,0);',(id,task))   
            conn.commit()
        return {"status":"creation successful"}
    except Exception as e:
        print("Error Encountered ",e)
        return erfc(e)


#fetch particular task details        
def getTaskDB():
     with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        return list(c.execute("select * from todolist;"))

#edit task details
def editTaskDB(task,id):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            id = generate_id()
            c.execute('update todolist set item = ? where id = ?;',(task,id))   
            conn.commit()
        return {"status":"updation successful"}
    except Exception as e:
        print("Error Encountered ",e)
        return erfc(e)

#change task status
def markTaskDB(id):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            check = list(c.execute('select * from todolist where "id" = ?;',(id)))
            if check != []:
                print(check)
                mark = 1 if int(check[0][2]) == 0 else 0
                
                c.execute('update todolist set status = ? where id = ?;',(mark,id))

                check = list(c.execute('select * from todolist where "id" = ?;',(id)))


                conn.commit()
                return {"status": str(check[0])}
            return {"ERROR":"Invalid ID"}
    except Exception as e:
        print("Error Encountered ",e)
        return erfc(e)

#remove task from database
def delTaskDB(id):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            check = c.execute('select * from todolist where "id" = ?',(id))   
            if list(check) != []:
                c.execute('delete from todolist where "id" = ?',(id))   
                conn.commit()
            else:
                return {"status":"No such Id"}
        return {"status":"deletion successful"}
    except Exception as e:
        print("Error Encountered ",e)
        return erfc(e)