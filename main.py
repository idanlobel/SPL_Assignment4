from DTOs.hat import hat
from DAOs.hats import hats
from DAOs.suppliers import suppliers
from DTOs.supplier import supplier
import sqlite3

file=open('config.txt' , mode='r')
lines=file.readlines()
get_numbers=lines[0].split(',')
number_of_hat_types=int(get_numbers[0])
number_of_suppliers=int(get_numbers[1])##actually no need to save this


lines=lines[1:]##skips first line
hats_table=hats.__init__(hats,conn)
suppliers_table=suppliers.__init__(suppliers,conn)
for line in lines:
    splitted_line=line.split(',')
    if number_of_hat_types !=0:
      created_hat=hat.__init__(hat,int(splitted_line[0]),splitted_line[1],int(splitted_line[2]),int(splitted_line[3]))
      hats_table.insert(created_hat)
      number_of_hat_types=number_of_hat_types-1
    else:
       created_supplier=supplier.__init__(supplier,int(splitted_line[0]),splitted_line[1])
       suppliers_table.insert(created_supplier)







