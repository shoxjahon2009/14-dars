import psycopg2
from parsing_lo import data_Base


# malumotlar bazasiga boglanish

data_base = psycopg2.connect(
    host='john.db.elephantsql.com',
    user='qnnwqdbg',
    database='qnnwqdbg',
    password='cKnFf15yejPuJPhAWZZli9uPB-URAtqc'
)
cursor = data_base.cursor()




for date in data_Base:
    product_name = date['Product_name']
    product_price = date['Product_price']
    product_image = date['Product_image']
    cursor.execute(f"""INSERT INTO users (name ,price,img) values ('{product_name}','{product_price}','{product_image}') """)
    print( product_name,product_price,product_image)



# data_base.commit()





#
#
# my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
#
# for key in my_dict:
#     value = my_dict[key]
#     print(f"The value for key '{key}' is: {value}")

