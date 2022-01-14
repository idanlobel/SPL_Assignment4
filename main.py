from DTOs.hat import hat
from DAOs.hats import hats
from DAOs.suppliers import suppliers
from DTOs.supplier import supplier
import _Repository
from DAOs.orders import orders
from DTOs.order import order
import sqlite3

file=open('config.txt' , mode='r')
lines=file.readlines()
get_numbers=lines[0].split(',')
number_of_hat_types=int(get_numbers[0])
number_of_suppliers=int(get_numbers[1])##actually no need to save this


lines=lines[1:]##skips first line

_Repository.repo.create_tables()

#building database:
for line in lines:
    splitted_line=line.split(',')
    if number_of_hat_types !=0:
      topping=splitted_line[1].rstrip('\n')
      created_hat=hat(int(splitted_line[0]),topping,int(splitted_line[2]),int(splitted_line[3]))
      _Repository.repo.hats.insert(created_hat)
      number_of_hat_types=number_of_hat_types-1
    else:
       name=splitted_line[1].rstrip('\n')
       created_supplier=supplier(int(splitted_line[0]),name)
       _Repository.repo.suppliers.insert(created_supplier)

#doing orders:
file=open('orders.txt' , mode='r')
lines=file.readlines()
order_id=1
output=open('summary.txt', mode='w')

for line in lines:
    splitted_line=line.split(',')
    topping=splitted_line[1].rstrip(('\n'))
    location=splitted_line[0].rstrip(('\n'))
    hat_id=_Repository.repo.hats.find(topping)# gits id of the hat to insert to order table
    first_supplierid=_Repository.repo.hats.get_first_supplierid_of_topping(topping)#git first id of supplier to do  -1 to the matching one
    _Repository.repo.hats.update_toppings_quantity(first_supplierid[0],topping)# substract quantitny by one
    _Repository.repo.hats.delete_if_zero()# delete if there is quantity 0 as a result of the substraction
    created_order=order(order_id,location,hat_id[0])
    order_id=order_id+1
    _Repository.repo.orders.insert(created_order)
    supplier_name=_Repository.repo.suppliers.find(first_supplierid[0])

    writeme=[]
    writeme.append(topping)
    writeme.append(' , ')
    writeme.append(supplier_name[0])
    writeme.append(' , ')
    writeme.append(location)
    writemeinstring=''.join(writeme)
    output.write(writemeinstring)
    output.write('\n')


output.close()




# DROP TABLE hats;
# DROP TABLE orders;
# DROP TABLE suppliers




