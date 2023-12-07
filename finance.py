from database import fetchone, fetchall


def create_user(username, password):
    query = "CALL create_user(%s, %s)"
    params = (username, password)
    result = fetchone(query, params)
    return result["id"]


def get_users():
    query = "SELECT * FROM get_users"
    result = fetchall(query)
    return result

def create_category(cat_name):
    query = "CALL create_category(%s)"
    params = (cat_name,)
    result = fetchone(query, params)
    return result["cat_id"]


def create_transaction(user_id, cat_id, amount, description, trans_date):
    query = "CALL create_transaction(%s, %s, %s, %s, %s)"
    params = (user_id, cat_id, amount, description, trans_date)
    result = fetchone(query, params)
    return result["trans_id"]


def get_transactions():
    query = "SELECT * FROM get_transactions"
    result = fetchall(query)
    return result


def get_transaction(trans_id):
    query = "SELECT * FROM get_transactions WHERE trans_id = %s"
    params = (trans_id,)
    result = fetchone(query, params)
    return result


def update_transaction(trans_id, user_id, cat_id, amount, description, trans_date):
    query = "CALL update_transaction(%s, %s, %s, %s, %s, %s)"
    params = (trans_id, user_id, cat_id, amount, description, trans_date)
    result = fetchone(query, params)
    return result["trans_id"]


def delete_transaction(trans_id):
    query = "CALL delete_transaction(%s)"
    params = (trans_id,)
    result = fetchone(query, params)
    return result["trans_id"]
