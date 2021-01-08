from db import db

def get_nouns():
    sql = "SELECT noun, englishNoun, gender FROM vocab where typeId = 0"
    result = db.session.execute(sql)
    return result.fetchall()


def insert_noun(gender, noun, englisNoun):
  
    sql = "INSERT INTO vocab (noun, englishNoun,gender, typeId) values (:noun,:englishNoun,:gender,:typeId)"
    db.session.execute(sql, {"noun":noun, "englishNoun":englisNoun, "gender":gender, "typeId":0})
    db.session.commit()
    return True
    

def get_verbs():
    sql = "SELECT id, noun, englishNoun,  FROM vocab where typeId = 1"