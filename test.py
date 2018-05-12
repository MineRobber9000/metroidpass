import metroidpass

password = ""
with open("testpass.txt") as f:
	password = "".join(l.rstrip() for l in f)

p = metroidpass.MetroidPass.decode(password)
