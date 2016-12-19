# -*- coding: utf-8 -*-
"""
    database
    ~~~~~~~~
    Interface to database of nummified strings.

    NummifyDatabase: Interface for interacting with a nummification database.
"""
import sqlite3


class NummifyDatabase(object):
    SCHEMA = '''
    CREATE TABLE IF NOT EXISTS nummified (
      message TEXT,
      nummification INTEGER
    );
    '''
    INDEX='''
    CREATE UNIQUE INDEX IF NOT EXISTS nummified_nummification
      ON nummified (message, nummification);
    '''

    def __init__(self, database_file):
        """Open the given database file and attempt to create schemas if they
        don't already exist.

        Arguments:
            database_file(str): The path to the database file.
        """
        self.db_file = database_file

    def __enter__(self):
        """Context manager entry point
        """
        self.db = sqlite3.connect(self.db_file)

        curr = self.db.cursor()
        curr.execute(self.SCHEMA)
        self.db.commit()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Context manager exit point
        """
        self.db.close()

    def add_entry(self, message, number):
        """Add an entry into the database for the given message and number.

        Arguments:
            message(str): The message
            number(int): Number corresponding to the given message
        """
        if not self.has_existing_entry(message, number):
            curr = self.db.cursor()
            curr.execute('''INSERT INTO nummified VALUES('{}', {})'''.format(
                message.upper(), number))
            self.db.commit()

    def has_existing_entry(self, message, number):
        curr = self.db.cursor()
        curr.execute('''
          SELECT * FROM nummified WHERE message='{}' AND nummification={}
        '''.format(message.upper(), number))
        return curr.fetchone() is not None

    def get_entries(self, number):
        """Get entries corresponding to the given number.

        Arguments:
            number(int): Number to look up

        Returns:
            list: List of number,message pairs
        """
        curr = self.db.cursor()
        query = '''SELECT * FROM nummified WHERE nummification={}'''.format(
            number)

        results = []
        for result in curr.execute(query):
            results.append(result)

        return results
