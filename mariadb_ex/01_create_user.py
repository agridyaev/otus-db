from mysql import connector
from lib.config import cfg
from lib.customer import customer
from lib.db_helpers import (
    create_customer, get_customer_id, delete_customer
)

conn = connector.connect(
    user=cfg.user,
    password=cfg.password,
    host=cfg.host,
    port=cfg.port,
    database=cfg.database
)

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

delete_customer(conn, customer_id=customer_id)

conn.close()
