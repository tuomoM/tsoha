CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT, uType INTEGER);
CREATE TABLE vocab (id SERIAL PRIMARY KEY, typeId INTEGER, noun TEXT, englishNoun TEXT, gender TEXT);
CREATE TABLE timeTypes (id SERIAL PRIMARY KEY, typeName TEXT);
CREATE TABLE verbForms (vocabId INTEGER REFERENCES vocab, timeType INTEGER REFERENCES timeTypes, fistP TEXT, secondP TEXT, thirdP TEXT, fourthP TEXT, PRIMARY KEY(vocabId,timeType));
CREATE TABLE userVerbs (userId INTEGER REFERENCES users, vocab INTEGER REFERENCES vocab, timeType INTEGER REFERENCES timeTypes , succesRate INTEGER, PRIMARY KEY(userId, vocab, timeType));
CREATE TABLE userNouns ( userId  INTEGER REFERENCES users, vocab INTEGER REFERENCES vocab, succesRate INTEGER, PRIMARY KEY(userId, vocab));