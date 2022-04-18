def create_customer(conn, first_name, last_name, email, telephone):
    query = """INSERT INTO oc_customer SET 
        customer_group_id = '1',
        store_id = '0',
        language_id = '1',
        firstname = ?,
        lastname = ?,
        email = ?,
        telephone = ?,
        fax = '',
        safe = '0',
        custom_field = '',
        token = '',
        code = '',
        salt = 'yNXIGdd1p',
        password = 'd1351a646f0fd4271258efba13da33be7ff1f3a8',
        newsletter = '0',
        ip = '172.18.0.1',
        status = '1',
        date_added = NOW()"""
    conn.cursor(prepared=True).execute(query, (first_name, last_name, email, telephone))


def delete_customer(conn, customer_id):
    query = "DELETE FROM oc_customer WHERE customer_id = ?"
    conn.cursor(prepared=True).execute(query, (customer_id, ))


def get_customer_id(conn, first_name, last_name, email=None, telephone=None):
    cursor = conn.cursor(prepared=True)
    query = """SELECT customer_id FROM oc_customer WHERE
        firstname = ?
        AND lastname = ?
        AND email = ?
        AND telephone = ?"""
    cursor.execute(query, (first_name, last_name, email, telephone))
    return cursor.fetchone()[0]


def add_to_wish_list(conn, customer_id, product_id):
    query = """INSERT INTO oc_customer_wishlist SET
        customer_id = ?,
        product_id = ?,
        date_added = NOW()"""
    conn.cursor(prepared=True).execute(query, (customer_id, product_id))


def remove_from_wish_list(conn, customer_id, product_id):
    query = """DELETE FROM oc_customer_wishlist WHERE
        customer_id = ? AND product_id = ?"""
    conn.cursor(prepared=True).execute(query, (customer_id, product_id))


def add_review(conn, author, customer_id, product_id, text, rating):
    query = """INSERT INTO oc_review SET
        author = ?,
        customer_id = ?,
        product_id = ?,
        text = ?,
        rating = ?,
        status = 1,
        date_added = NOW(),
        date_modified = NOW()"""
    conn.cursor(prepared=True).execute(query, (author, customer_id, product_id, text, rating))


def get_review_id(conn, customer_id, product_id):
    cursor = conn.cursor(prepared=True)
    query = """SELECT review_id FROM oc_review
        WHERE customer_id = ? AND product_id = ?"""
    cursor.execute(query, (customer_id, product_id))
    return cursor.fetchone()[0]


def remove_review(conn, review_id):
    query = "DELETE FROM oc_review WHERE review_id = ?"
    conn.cursor(prepared=True).execute(query, (review_id, ))
