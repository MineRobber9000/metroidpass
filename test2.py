import metroidpass

def split(s):
	for i in range(0,len(s),6):
		yield s[i:i+6]

p = metroidpass.MetroidPass()
p.samus_in_swimsuit=True
print(" ".join(split(p.encode())))
