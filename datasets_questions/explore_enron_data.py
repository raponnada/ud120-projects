#!/usr/bin/python
# coding=utf-8

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#for name, feature in enron_data.items():
#   print(name,feature)


# 13. qz - # persons in data set
# print len(enron_data)

# 14. qz - each person how many features
# print len(enron_data.items()[1][1])
# for name, feature in enron_data.items():
#   print(name,len(feature))

# 15. qz - Finding POIs In The Enron Data
# print (len({name:item['poi'] for name,item in enron_data.items() if item['poi']==1}))

# 16.qz - How Many POIs Exist?
# count #names from ../final_project/poi_email_addresses.py

# 18. qz - What is the total value of the stock belonging to James Prentice?
# print enron_data['PRENTICE JAMES']['total_stock_value']

# 19. qz - How many email messages do we have from Wesley Colwell to persons of interest?
# print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

# 20. qz - What’s the value of stock options exercised by Jeffrey K Skilling?
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]