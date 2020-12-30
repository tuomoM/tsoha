from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username,password):
    sql = "SELECT password, id, uType FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            session["user_type"] = user[2]
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username,password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password,uType) VALUES (:username,:password,:uType)"
        db.session.execute(sql, {"username":username,"password":hash_value,"uType":0})
        db.session.commit()
    except:
        return False
    return login(username,password)

def user_id():
    return session.get("user_id",0)
