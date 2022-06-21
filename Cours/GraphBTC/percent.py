# !!!!!!! don't work !!!!!!!


f = input("Entrez les deux et mettez ; pour separer:\n")

g = f.split(';')

c = float(float(g[0])*100/float(g[1]))

if float(100 - c) >= 0:
    print("+" + str(100 - c) + "%")
else:
    print(str(100 - c) + "%")