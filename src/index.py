#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import dataset

import json

host = "127.0.0.1"
port = 5432
username = "test"
password = "test"

dbname = "test"
tableName = "test"

try:

    db = dataset.connect(f"postgresql://{username}:{password}@{host}:{port}/{dbname}")

    table = db[tableName]

    # Insertando un sólo documento en la tabla

    doc = {
        "author": "Lastseal",
        "text": "Ejemplo de documento",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.utcnow()
    }

    table.insert(doc)

    print( table.find_one() )

    # Insertando múltiples documentos

    docs = [
        {
            "author": "developer 1",
            "text": "Primer documento",
            "tags": ["bulk", "insert"],
            "date": datetime(2021, 12, 1, 11, 14)
        },
        {
            "author": "developer 2",
            "text": "Segundo documento",
            "date": datetime(2021, 12, 2, 10, 45)
        }
    ]

    table.insert_many(docs)

    for doc in table.find():
        print(doc)

except Exception as ex:
    print(ex)
