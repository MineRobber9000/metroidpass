# Rotate left: 0b1001 --> 0b0011
rrol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
# Rotate right: 0b1001 --> 0b1100
rror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def ror(x,b,m=8):
	x = rror(x,b,m)
	c = 1 if (x&(1<<(m-1)))==(1<<(m-1)) else 0
	return (x,c)

def rol(x,b,m=8):
	x = rrol(x,b,m)
	c = 1 if (x&1)==1 else 0 # rotated bit is at bit 0 regardless of maximum
	return (x,c)
