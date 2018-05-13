import metroidpass

password = ""
with open("testpass.txt") as f:
	password = "".join(l.rstrip() for l in f)

p = metroidpass.MetroidPass.decode(password)
print("Samus in swimsuit" if p.samus_in_swimsuit else "Samus not in swimsuit")
print("Password generated matches password input" if p.encode()==password else "Password generated does not match password input")
