import bwr, enum
def msp(l,c):
	if c == 0:
		return l
	copy = l[0]
	carry = 0
	for i in range(16):
		copy = l[0]
		x,ca = bwr.ror(l[i],1)
		x = x | carry
		carry = ca
		l[i]=x
	x,ca = bwr.ror(copy,1)
	x = x | carry
	l[0] = x
	return msp(l,(c-1))

def mspd(l,c):
	if c == 0:
		return l
	copy = l[0]
	carry = 0
	for i in range(16):
		copy = l[0]
		x,ca = bwr.rol(l[i],1)
		x = x | carry
		carry = ca
		l[i]=x
	x,ca = bwr.rol(copy,1)
	x = x | carry
	l[0] = x
	return mspd(l,(c-1))

class MetroidPasswordBitsEnum(enum.Enum):
	def __init__(self):
		super().__init__()
		self.define('maru_mari_taken')
		self.define('missile_container_brinstar_1')
		self.define('red_door_long_beam')
		self.define('red_door_tourian_bridge')
		self.define('energy_tank_brinstar_1')
		self.define('red_door_bombs')
		self.define('bombs_taken')
		self.define('red_door_ice_beam_brinstar')
		self.define('missile_container_brinstar_2')
		self.define('energy_tank_brinstar_2')
		self.define('red_door_varia')
		self.define('varia_taken')
		self.define('energy_tank_brinstar_3')
		self.define('missile_container_norfair_1')
		self.define('missile_container_norfair_2')
		self.define('red_door_ice_beam_norfair')
		self.define('missile_container_norfair_3')
		self.define('missile_container_norfair_4')
		self.define('missile_container_norfair_5')
		self.define('missile_container_norfair_6')
		self.define('missile_container_norfair_7')
		self.define('missile_container_norfair_8')
		self.define('missile_container_norfair_9')
		self.define('red_door_high_jump_boots')
		self.define('high_jump_boots_taken')
		self.define('red_door_screw_attack')
		self.define('screw_attack_taken')
		self.define('missile_container_norfair_10')
		self.define('missile_container_norfair_11')
		self.define('red_door_wave_beam')
		self.define('energy_tank_norfair')
		self.define('missile_container_norfair_12')
		self.define('red_door_kraid_lair_1')
		self.define('missile_container_kraid_lair_1')
		self.define('missile_container_kraid_lair_2')
		self.define('red_door_kraid_lair_2')
		self.define('energy_tank_kraid_lair')
		self.define('red_door_kraid_lair_3')
		self.define('red_door_kraid_lair_4')
		self.define('missile_container_kraid_lair_3')
		self.define('missile_container_kraid_lair_4')
		self.define('red_door_kraid_room')
		self.define('energy_tank_kraid_room')
		self.define('missile_container_ridley_lair_1')
		self.define('red_door_ridley_lair')
		self.define('energy_tank_ridley_lair')
		self.define('missile_container_ridley_lair_2')
		self.define('yellow_door_in_ridley_room')
		self.define('energy_tank_room_behind_ridley')
		self.define('missile_container_ridley_lair_3')
		self.define('yellow_door_tourian')
		self.define('red_door_tourian_1')
		self.define('red_door_tourian_2')
		self.define('zebetite_1_killed')
		self.define('zebetite_2_killed')
		self.define('zebetite_3_killed')
		self.define('zebetite_4_killed')
		self.define('zebetite_5_killed')
		self.define('mother_brain_killed')
		self.define('unknown_1')
		self.define('unknown_2')
		self.define('unknown_3')
		self.define('unknown_4')
		self.define('unknown_5')
		self.define('start_in_norfair')
		self.define('start_in_kraid_lair')
		self.define('start_in_ridley_lair')
		self.define('reset')
		self.define('unknown_6')
		self.define('unknown_7')
		self.define('unknown_8')
		self.define('samus_in_swimsuit')
		self.define('samus_has_bombs')
		self.define('samus_has_high_jump_boots')
		self.define('samus_has_long_beam')
		self.define('samus_has_screw_attack')
		self.define('samus_has_maru_mari')
		self.define('samus_has_varia')
		self.define('samus_has_wave_beam')
		self.define('samus_has_ice_beam')
		self.define('missile_count_plus_1')
		self.define('missile_count_plus_2')
		self.define('missile_count_plus_4')
		self.define('missile_count_plus_8')
		self.define('missile_count_plus_16')
		self.define('missile_count_plus_32')
		self.define('missile_count_plus_64')
		self.define('missile_count_plus_128')
#		self.define('game_age_32-bit_value_--_low_bit')
		for i in range(32,0,-1):
			self.define("game_age_bit_{!s}".format(i-1))
		self.define('unknown_9')
		self.define('unknown_10')
		self.define('unknown_11')
		self.define('unknown_12')
		self.define('ridley_killed')
		self.define('ridley_statue_raised')
		self.define('kraid_killed')
		self.define('kraid_statue_raised')
		assert self.v==128,"I fucked it up somewhere damn it"

bits = MetroidPasswordBitsEnum()

def get_bit_loc(n):
	return (n//8,n%8)

def get_bit(l,n,c=None):
	if c is None:
		n, c = get_bit_loc(n)
	return (l[n]&(1<<c))==(1<<c)

def bitfield(*bits):
	ret = 0
	for i in range(len(bits)):
		if bits[i]: ret = ret | (1<<i)
	return ret
