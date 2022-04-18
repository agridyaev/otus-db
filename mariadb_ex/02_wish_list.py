import mariadb
from lib.config import cfg
from lib.customer import customer
from lib.db_helpers import (
    create_customer, delete_customer, get_customer_id,
    add_to_wish_list, remove_from_wish_list
)

conn = mariadb.connect(
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

add_to_wish_list(conn, customer_id, product_id)
remove_from_wish_list(conn, customer_id, product_id)

delete_customer(conn, customer_id=customer_id)

conn.close()
