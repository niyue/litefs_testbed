#!/bin/env python

import sqlite3

def insert(node):
    con = sqlite3.connect(f"./nodes/{node}/mnt/test.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
    cur.execute(
    """
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
    """
    )
    con.commit()

def read_tables(node):
    con = sqlite3.connect(f"./nodes/{node}/mnt/test.db")
    cur = con.cursor()
    res = cur.execute("SELECT name FROM sqlite_master")
    row = res.fetchone()
    print("tables:", row)

insert("n1")