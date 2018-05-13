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
	for i in range(15,-1,-1):
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

def get_bit_loc(n,b=8):
	return (n//b,n%b)

def get_bit(l,n,c=None,b=8):
	if c is None:
		n, c = get_bit_loc(n,b)
	return (l[n]&(1<<c))==(1<<c)

#def bitfield(*bits):
#	ret = 0
#	for i in range(len(bits)):
#		if bits[i]: ret = ret | (1<<i)
#	return ret

#def bits_to_list(l,b=8):
#	return [get_bit(l,n,None,b) for n in range(len(l)*b)]

def regroup(l,ob=8,nb=8):
	ret = []
	bs = "".join(bin(x,ob) for x in l)
	for i in range(0,len(bs),nb):
		ret.append(int(bs[i:i+nb],2))
	return ret

def bin(x,b=8):
	ret = ""
	for i in range((b-1),-1,-1):
		ret += "1" if (x&(1<<i))==(1<<i) else "0"
	return ret

def six_to_eight(l):
	return regroup(l,6,8)
#	bs = "".join(bin(x,6) for x in l)
#	ret = []
#	for i in range(0,len(bs),8):
#		ret.append(int(bs[i:i+8],2))
#	return ret

def eight_to_six(l):
	return regroup(l,8,6)

def is_iterable(o):
	try:
		m = iter(o)
		return True
	except:
		return False

def joinel(*args):
	ret = []
	for i in args:
		if is_iterable(i):
			ret.extend(x for x in i)
		else:
			ret.append(i)
	return ret

class MetroidPass:
	ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?-"
	def __init__(self,bytevals=None,shift=None,checksum=None):
		if bytevals is None:
			bytevals = [0 for x in range(16)]
		if shift is None:
			shift = 0
		self.bytevals = bytevals
		self.shift = 0
		if checksum is None:
			self.calc_checksum()
		else:
			self.checksum = checksum
		self.is_debug = False

	def calc_checksum(self):
		cs = 0
		for i in self.bytevals:
			cs=(cs+i)%256
		cs=(cs+self.shift)%256
		self.checksum = cs

	@classmethod
	def decode(cls,password):
		if len(password)<24:
			password = cls.pad(password)
		bts = [cls.ALPHABET.index(x) if x!=" " else 255 for x in password]
		for i in range(len(bts)):
			if bts[i]==255:
				bts[i-1]|=3 # 3 = 0b11
		ret = cls()
		bts = six_to_eight(bts)
		ret.shift = bts[16]
		ret.bytevals = mspd(bts[:16],ret.shift)
		if password.startswith("NARPASSWORD00000"):
			ret.is_debug = True
			return ret
		ret.calc_checksum()
		if ret.checksum!=bts[17]:
			print("WARNING: Given password is NOT valid! ({!s}!={!s})".format(ret.checksum,bts[17]))
		return ret

	def encode(self):
		if self.is_debug:
			return self.pad("NARPASSWORD00000")
		self.calc_checksum()
		passdata = joinel(self.bytevals,self.shift,self.checksum)
		passdata = msp(passdata,self.shift)
		passdata = eight_to_six(passdata)
		return "".join(self.ALPHABET[x] for x in passdata)

	def start_in(self,loc=None):
		if loc is None:
			if p.reset:
				return "reset"
			starts_in = (self.start_in_norfair,self.start_in_kraid_lair,self.start_in_ridley_lair)
			if starts_in==(False,False,False):
				return "beginning"
			elif starts_in==(True,False,False):
				return "norfair"
			elif starts_in==(False,True,False):
				return "kraid_lair"
			elif starts_in==(False,False,True):
				return "ridley_lair"
			elif starts_in==(True,True,False):
				return "tourian"
		else:
			nor = False
			kraid = False
			ridley = False
			if loc=="norfair":
				nor = True
			elif loc=="kraid_lair":
				kraid = True
			elif loc=="ridley_lair":
				ridley = True
			elif loc=="tourian":
				nor = True
				kraid = True
			self.start_in_norfair = nor
			self.start_in_kraid_lair = kraid
			self.start_in_ridley_lair = ridley
			self.reset = False

	@classmethod
	def pad(cls,password,l=24):
		return (password+(cls.ALPHABET[0]*l))[:l]

	def __getattr__(self,k):
		shortcuts = dict(missiles=10)
		if k in bits.defines:
			return get_bit(self.bytevals,bits.defines[k])
		elif k in shortcuts:
			return self.bytevals[shortcuts[k]]
		return object.__getattr__(self,k)

	def __setattr__(self,k,v):
		shortcuts = dict(missiles=10)
		if k in bits.defines:
			i,p = get_bit_loc(bits.defines[k])
			if v:
				self.bytevals[i]|=(1<<p)
			else:
				self.bytevals[i]&=~(1<<p)
		elif k in shortcuts:
			self.bytevals[shortcuts[k]] = v
		return object.__setattr__(self,k,v)
