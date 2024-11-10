import sqlite3

def connect(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    return conn, cur







def create_users_table():
    conn, cur = connect('../translator.db')
    sql = '''
        create table if not exists users (
            user_id INTEGER PRIMARY KEY autoincrement,
            chat_id bigint not null    
        );
        
    '''
    cur.execute(sql)
    conn.commit()
    conn.close()
    print('users table created')
#
# create_users_table()

def create_translation_table():
    conn, cur = connect('../translator.db')
    sql = '''
        create table if not exists translation (
            translator_id INTEGER PRIMARY KEY autoincrement,
            original_text,
            translated_text,
            code_from text,
            code_to text,
            is_fav boolean default false,
            user_id INTEGER REFERENCES users(user_id)
        );
    
    '''
    cur.execute(sql)
    conn.commit()
    conn.close()
    print('translation table created')

# create_translation_table()


def get_user_id(chat_id):
    conn, cur = connect('translator.db')
    sql = 'select user_id from users where chat_id = ?'
    user = cur.execute(sql, (chat_id,)).fetchone()
    if user is None:
        return 0, False
    return user[0], True

def add_user(chat_id):
    user_id, exists = get_user_id(chat_id)
    sql = ('insert into users (chat_id)'
           ' values (?)')
    conn, cur = connect('translator.db')

    if not exists:
        cur.execute(sql, (chat_id,))
        conn.commit()
        conn.close()


def add_translation(
        original,
        translated,
        code_from,
        code_to,
        chat_id

):
    conn, cur = connect('translator.db')
    user_id, _ = get_user_id(chat_id)
    sql = '''
        insert into translation (original, translated, code_from, code_to, user_id) 
        values (?, ?, ?, ?, ?) returning translation_id;        
    '''
    _id = cur.execute(sql, (original, translated, code_from, code_to, user_id)).fetchone()
    conn.commit()
    conn.close()
    return _id