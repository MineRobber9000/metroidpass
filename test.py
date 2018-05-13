import metroidpass

password = ""
with open("testpass.txt") as f:
	password = "".join(l.rstrip() for l in f)

p = metroidpass.MetroidPass.decode(password)
print("Samus in swimsuit" if p.samus_in_swimsuit else "Samus not in swimsuit")
print("Password generated matches password input" if p.encode()==password else "Password generated does not match password input")
print("{!s} missiles".format(p.missiles))
print("Ridley's Lair" if p.start_in_ridley_lair else "umm")
energy_tanks = 0
if p.energy_tank_kraid_room:
	energy_tanks+=1
if p.energy_tank_ridley_lair:
	energy_tanks+=1
if p.energy_tank_kraid_lair:
	energy_tanks+=1
if p.energy_tank_brinstar_1:
	energy_tanks+=1
if p.energy_tank_brinstar_2:
	energy_tanks+=1
if p.energy_tank_brinstar_3:
	energy_tanks+=1
if p.energy_tank_norfair:
	energy_tanks+=1
if p.energy_tank_room_behind_ridley:
	energy_tanks+=1
print("{!s} energy tanks".format(energy_tanks))
