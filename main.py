'''
Name: Noah Estrada-Rand
Student ID#: 2272490
Chapman email: estra146@mail.chapman.edu
Course Number and Section: CPSC-408-01
Assignment: In-class MongoDB Assignment
'''

import pymongo

CONNECTION_STRING = 'mongodb+srv://noah_e:theHills>@cluster0-mif3b.gcp.mongodb.net/test?retryWrites=true&w=majority'

client = pymongo.MongoClient("mongodb+srv://noah_e:theHills@cluster0-mif3b.gcp.mongodb.net/test?retryWrites=true&w=major"\
                                "ity&ssl_cert_reqs=CERT_NONE")
db = client['in_class']

###print records
for s in db.stud_records.find():
    print(s)
#
###finding a record
# for s in db.stud_records.find({"Major":{"$eq":"Pr & Ad"}}):
#     print(s)
#
#adding in new records
# db.stud_records.insert_one({"Firstname":"Isabel","Wiemken":"Estrada-Rand","GPA":3.5,"Major":"Pr & Ad"})