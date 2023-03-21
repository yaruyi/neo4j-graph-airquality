#generate financial transaction 
import numpy as np
import random
import pandas as pd

#unique transaction id's
transaction_id = [i for i in range(1,101)]

#vendor/customer number
vendor_number = np.random.randint(low = 1, high = 2500, size = (100,))

#transaction amount
transaction_amount = np.random.randint(low = 20, high = 1250, size = (100))

#transaction type
transaction_types = ['cash_withdrawl', 'cash_deposit','transfer_domestic','transfer_international']

#generate list of random integers
random_integers = [random.randint(0,3) for i in range(0,100)]
transaction_list = [transaction_types[i] for i in random_integers]


transaction_data = {"transaction_ID": transaction_id,
                   "vendor_number" : list(vendor_number),
                   "transaction_amount" : list(transaction_amount),
                    "transaction_type" : transaction_list,}


transaction_DataFrame = pd.DataFrame(transaction_data)

print(transaction_DataFrame[:1])

####### import data into neo4j ##### 
from neo4j import GraphDatabase

transaction_list = transaction_DataFrame.values.tolist()

transaction_execution_commands = []

for i in transaction_list:
    neo4j_create_statemenet = "create (t:Transaction {transaction_id:" + str(i[0]) +", vendor_number:  " + str(i[1]) +", transaction_amount: " + str(i[2]) +", transaction_type: '" + str(i[3]) + "'})"
    transaction_execution_commands.append(neo4j_create_statemenet)

    
def execute_transactions(transaction_execution_commands):
    data_base_connection = GraphDatabase.driver(uri = "bolt://localhost:7687", auth=("neo4j", "password"))
    session = data_base_connection.session()    
    for i in transaction_execution_commands:
        session.run(i)

#print(transaction_execution_commands[:4])
execute_transactions(transaction_execution_commands)