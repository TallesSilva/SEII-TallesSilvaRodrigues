with open("Modulos/teste.txt", "r") as f:
    size = 5
    f_text = f.read(size)
    pass

with open("Modulos/teste2.py", "w") as w:
    w.write(f_text)
    pass

print(f.closed)
print(w.closed)