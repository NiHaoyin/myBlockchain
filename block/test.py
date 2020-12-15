import time
import hashlib

s = hashlib.sha256()
s.update("nihao".encode("utf-8"))
b = s.hexdigest()
print(b.startswith("5e7"))
print(type(b))