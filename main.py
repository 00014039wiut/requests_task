import requests
import psycopg2

url = "https://dummyjson.com/users"
r = requests.get(url)

conn = psycopg2.connect(dbname='new_db',
                        user='postgres',
                        password='Sql7575',
                        host='localhost',
                        port=5432)

curr = conn.cursor()

create_table_query = """create table company_users(
ID serial primary key,
firstName varchar(50),
lastName varchar(50),
maidenName varchar(50),
age int,
gender varchar(10),
email varchar(50),
phone varchar(50),
username varchar(50),
password varchar(50),
birthDate varchar(50),
image varchar(255),
bloodGroup varchar(50),
height int,
weight float,
eyeColor varchar(50),
hairColor varchar(50),
hairType varchar(50))"""

# curr.execute(create_table_query)
# conn.commit()

insert_into_query = """insert into company_users(firstName, lastName, maidenName, age, gender, email, phone, 
username, password, birthDate, image, bloodGroup, height, weight, eyeColor, hairColor, hairType) values (%s,%s,%s,%s,
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); """

for user in r.json()["users"]:
    curr.execute(insert_into_query, (user["firstName"], user["lastName"], user["maidenName"], str(user["age"]), user["gender"],
                                     user["email"], user["phone"], user["username"], user["password"], user["birthDate"],
                                     user["image"], user["bloodGroup"], str(user["height"]), str(user["weight"]), user["eyeColor"],
                                     user["hair"]["color"], user["hair"]["type"]))
    conn.commit()
