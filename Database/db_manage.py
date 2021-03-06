import os
import sqlite3


class ManageDB:
    def __init__(self, db_file_name):
        curr_path = os.path.dirname(os.path.abspath(__file__))
        self.db_full_path = os.path.join(curr_path, db_file_name)
        self.comment_record = None
        self.connection = None
        self.connect_create_db()

    def connect_create_db(self):
        if os.path.isfile(self.db_full_path):
            # connection to database file
            self.connection = sqlite3.connect(self.db_full_path)
            # database cursor object
            self.comment_record = self.connection.cursor()
        else:  # if it doesn't, create it
            self.connection = sqlite3.connect(self.db_full_path)
            self.comment_record = self.connection.cursor()
            self.comment_record.execute('''CREATE TABLE comments(comment text)''')

    def get_db(self):
        return self.connection, self.comment_record, self

    def insert_db(self, comment_id):
        self.comment_record.execute(
            'INSERT INTO comments VALUES (?);', (comment_id,))
        self.connection.commit()

    def query_db(self, comment_id):
        self.comment_record.execute(
            "SELECT * FROM comments WHERE comment=?", (comment_id,))
        return self.comment_record.fetchone()
