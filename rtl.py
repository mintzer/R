# coding: utf-8

import os
replacement = '<html dir="rtl" lang="" xml:lang=""><link rel="shortcut icon" href="rstudio.svg" />'
for dname, dirs, files in os.walk(r"C:\R\R"):
    for fname in files:
        if fname[-5:] == '.html':
            print(fname)
            fpath = os.path.join(dname, fname)
            with open(fpath) as f:
                s = f.read()
            s = s.replace('<html lang="" xml:lang="">', replacement)
            with open(fpath, "w") as f:
                f.write(s)

replacement2 = 'מה תרצי לחפש? (Enter כדי לעבור בין התוצאות)'
replacement3 = 'הקלד כדי לחפש'
for dname, dirs, files in os.walk(r"C:\R\R"):
    for fname in files:
        if fname[-3:] == '.js':
            print(fname)
            fpath = os.path.join(dname, fname)
            with open(fpath) as f:
                s = f.read()
            s = s.replace('Type to search (Enter for navigation)', replacement2)
            s = s.replace('Type to search', replacement3)
            with open(fpath, "w") as f:
                f.write(s)



# --- Data pipeline configuration ---
import requests

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://localhost:5432/myapp")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
JWT_SECRET = os.environ.get("JWT_SECRET")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
