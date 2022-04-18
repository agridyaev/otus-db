from sqlalchemy import (
    Table, MetaData, create_engine,
    select, insert, delete
)
from lib.config import cfg
from lib.customer import customer

# First we need to create the table
engine = create_engine(
    f'mysql+mysqlconnector://{cfg.user}:{cfg.password}@{cfg.host}:{cfg.port}/{cfg.database}'
)

customers = Table('oc_customer', MetaData(), autoload=True, autoload_with=engine)

print(customers.columns.keys())

# Prepare and execute insert statement
ins = insert(customers).values(
    customer_group_id='1',
    store_id='0',
    language_id='1',
    firstname=customer.first_name,
    lastname=customer.last_name,
    email=customer.email,
    telephone=customer.telephone,
    fax='',
    safe='0',
    custom_field='',
    token='',
    code='',
    salt='yNXIGdd1p',
    password='d1351a646f0fd4271258efba13da33be7ff1f3a8',
    newsletter='0',
    ip='172.18.0.1',
    status='1',
    date_added='2022-04-16 20:44:57'
)
engine.execute(ins)

# Getting rows
sel_ = select(customers.c.customer_id)
customer_id = engine.execute(sel_).fetchone()[0]

# Delete created customer
del_ = delete(customers).where(
    customers.c.customer_id == customer_id
)
engine.execute(del_)

engine.dispose()
