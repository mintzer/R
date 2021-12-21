import os
replacement = '<html dir="rtl" lang="" xml:lang="">}'
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