from DTOs.hat import hat
from DAOs.hats import hats
from DAOs.suppliers import suppliers
from DTOs.supplier import supplier
import _Repository
import sqlite3

file=open('config.txt' , mode='r')
lines=file.readlines()
get_numbers=lines[0].split(',')
number_of_hat_types=int(get_numbers[0])
number_of_suppliers=int(get_numbers[1])##actually no need to save this


lines=lines[1:]##skips first line

_Repository.repo.create_tables()

for line in lines:
    splitted_line=line.split(',')
    if number_of_hat_types !=0:
      created_hat=hat(int(splitted_line[0]),splitted_line[1],int(splitted_line[2]),int(splitted_line[3]))
      _Repository.repo.hats.insert(created_hat)
      number_of_hat_types=number_of_hat_types-1
    else:
       created_supplier=supplier(int(splitted_line[0]),splitted_line[1])
       _Repository.repo.suppliers.insert(created_supplier)







