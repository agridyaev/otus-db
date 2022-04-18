from mysql import connector
from lib.config import cfg
from lib.customer import customer
from lib.db_helpers import (
    create_customer, delete_customer, get_customer_id,
    add_review, get_review_id, remove_review
)

conn = connector.connect(
    user=cfg.user,
    password=cfg.password,
    host=cfg.host,
    port=cfg.port,
    database=cfg.database
)

product_id = '42'  # Apple Cinema 30"

create_customer(
    conn,
    first_name=customer.first_name,
    last_name=customer.last_name,
    email=customer.email,
    telephone=customer.telephone
)

customer_id = get_customer_id(
    conn,
    first_name=customer.first_name,
    last_name=customer.last_name,
    email=customer.email,
    telephone=customer.telephone
)

add_review(
    conn,
    author=f'{customer.first_name} {customer.last_name}',
    customer_id=customer_id,
    product_id=product_id,
    text='This is really nice product! I like it very much!',
    rating='5'
)

review_id = get_review_id(
    conn,
    customer_id=customer_id,
    product_id=product_id
)

remove_review(conn, review_id)
delete_customer(conn, customer_id=customer_id)

conn.close()
