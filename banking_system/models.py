# Data models and database operations

from db import get_connection

def create_account(name, initial_balance=0.0):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO accounts (name, balance) VALUES (?, ?)', (name, initial_balance))
    conn.commit()
    account_id = cursor.lastrowid
    conn.close()
    return account_id

def get_account(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM accounts WHERE id=?', (account_id,))
    account = cursor.fetchone()
    conn.close()
    return account

def update_balance(account_id, amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE accounts SET balance = balance + ? WHERE id=?', (amount, account_id))
    conn.commit()
    conn.close()

def record_transaction(account_id, trans_type, amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO transactions (account_id, type, amount) VALUES (?, ?, ?)', (account_id, trans_type, amount))
    conn.commit()
    conn.close()

def get_transactions(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions WHERE account_id=? ORDER BY timestamp DESC', (account_id,))
    transactions = cursor.fetchall()
    conn.close()
    return transactions