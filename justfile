#!/usr/bin/env just --justfile

set dotenv-load := true

start node:
  litefs --config nodes/{{node}}/litefs.yml 

app:
  python app.py

clean:
  rm -fr nodes/n1/mnt nodes/n1/data nodes/n2/mnt nodes/n2/data

db node:
  sqlite3 nodes/{{node}}/mnt/test.db

