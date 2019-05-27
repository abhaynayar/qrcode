import numpy as np
from matplotlib import pyplot as plt

# https://www.thonky.com/qr-code-tutorial/

# document
# console helper outputs

'''
Glossary

ccp_?	character capacities array (? => ecl)
mode	mode of data {N,A,B,K}
inp		input text by the user to be converted
ecl		error correction level {L,M,Q,H}
v		version
n		dimension
out		output data
img		final image
cci		character count indicator => determines in padded binary how many characters in input
'''

''' ENCODING DATA '''

ccp_a = [[25,47,77,114,154,195,224,279],
		 [20,38,61,90,122],
		 [16,29,47],
		 [10,20]] # and so on, ...

# for now input is fixed
mode = 'A'
inp = 'HELLO WORLD'
ecl = 'M'

''' Determining smallest version '''

v = 1

if(mode == 'A'):
	if(ecl == 'L'):
		size = len(inp) # max is 4296 (40L)
		for i in range(40):
			if(size < ccp_a[0][i]):
				v=i+1
				break



n = (((v-1)*4)+21)

out = ''

''' Add Mode Indicator '''
if(mode == 'A'):
	out += '0010'

''' Add Character Count Indicator '''
ccpad = 0
if(1<=v<=9): # and so on
	if(mode == 'A'): # and so on
		ccpad = 9

out += ("{0:b}".format(len(inp))).zfill(ccpad)


''' Encode Data '''

alpha_dict = {
	'0': 0,
	'1': 1,
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'A': 10,
	'B': 11,
	'C': 12,
	'D': 13,
	'E': 14,
	'F': 15,
	'G': 16,
	'H': 17,
	'I': 18,
	'J': 19,
	'K': 20,
	'L': 21,
	'M': 22,
	'N': 23,
	'O': 24,
	'P': 25,
	'Q': 26,
	'R': 27,
	'S': 28,
	'T': 29,
	'U': 30,
	'V': 31,
	'W': 32,
	'X': 33,
	'Y': 34,
	'Z': 35,
	' ': 36,
	'$': 37,
	'%': 38,
	'*': 39,
	'+': 40,
	'-': 41,
	'.': 42,
	'/': 43,
	':': 44
}

for x in range(1,len(inp),2):
	sum = alpha_dict[inp[x-1]] * 45 + alpha_dict[inp[x]]
	out += ("{0:b}".format(sum)).zfill(11)

if(len(inp)%2 == 1): # if it's odd
	out += ("{0:b}".format(alpha_dict[inp[-1]])).zfill(6)


''' Codewords & Padding '''

total_cwd = {
	"1-L":	19  ,
	"1-M":	16  ,
	"1-Q":	13  ,
	"1-H":	9   ,
	"2-L":	34  ,
	"2-M":	28  ,
	"2-Q":	22  ,
	"2-H":	16  ,
	"3-L":	55  ,
	"3-M":	44  ,
	"3-Q":	34  ,
	"3-H":	26  ,
	"4-L":	80  ,
	"4-M":	64  ,
	"4-Q":	48  ,
	"4-H":	36  ,
	"5-L":	108 ,
	"5-M":	86  ,
	"5-Q":	62  ,
	"5-H":	46  ,
	"6-L":	136 ,
	"6-M":	108 ,
	"6-Q":	76  ,
	"6-H":	60  ,
	"7-L":	156 ,
	"7-M":	124 ,
	"7-Q":	88  ,
	"7-H":	66  ,
	"8-L":	194 ,
	"8-M":	154 ,
	"8-Q":	110 ,
	"8-H":	86  ,
	"9-L":	232 ,
	"9-M":	182 ,
	"9-Q":	132 ,
	"9-H":	100 ,
	"10-L":	274	,
	"10-M":	216	,
	"10-Q":	154	,
	"10-H":	122	,
	"11-L":	324	,
	"11-M":	254	,
	"11-Q":	180	,
	"11-H":	140	,
	"12-L":	370	,
	"12-M":	290	,
	"12-Q":	206	,
	"12-H":	158	,
	"13-L":	428	,
	"13-M":	334	,
	"13-Q":	244	,
	"13-H":	180	,
	"14-L":	461	,
	"14-M":	365	,
	"14-Q":	261	,
	"14-H":	197	,
	"15-L":	523	,
	"15-M":	415	,
	"15-Q":	295	,
	"15-H":	223	,
	"16-L":	589	,
	"16-M":	453	,
	"16-Q":	325	,
	"16-H":	253	,
	"17-L":	647	,
	"17-M":	507	,
	"17-Q":	367	,
	"17-H":	283	,
	"18-L":	721	,
	"18-M":	563	,
	"18-Q":	397	,
	"18-H":	313	,
	"19-L":	795	,
	"19-M":	627	,
	"19-Q":	445	,
	"19-H":	341	,
	"20-L":	861	,
	"20-M":	669	,
	"20-Q":	485	,
	"20-H":	385	,
	"21-L":	932	,
	"21-M":	714	,
	"21-Q":	512	,
	"21-H":	406	,
	"22-L":	1006,
	"22-M":	782	,
	"22-Q":	568	,
	"22-H":	442	,
	"23-L":	1094,
	"23-M":	860	,
	"23-Q":	614	,
	"23-H":	464	,
	"24-L":	1174,
	"24-M":	914	,
	"24-Q":	664	,
	"24-H":	514	,
	"25-L":	1276,
	"25-M":	1000,
	"25-Q":	718	,
	"25-H":	538	,
	"26-L":	1370,
	"26-M":	1062,
	"26-Q":	754	,
	"26-H":	596	,
	"27-L":	1468,
	"27-M":	1128,
	"27-Q":	808	,
	"27-H":	628	,
	"28-L":	1531,
	"28-M":	1193,
	"28-Q":	871	,
	"28-H":	661	,
	"29-L":	1631,
	"29-M":	1267,
	"29-Q":	911	,
	"29-H":	701	,
	"30-L":	1735,
	"30-M":	1373,
	"30-Q":	985	,
	"30-H":	745	,
	"31-L":	1843,
	"31-M":	1455,
	"31-Q":	1033,
	"31-H":	793	,
	"32-L":	1955,
	"32-M":	1541,
	"32-Q":	1115,
	"32-H":	845	,
	"33-L":	2071,
	"33-M":	1631,
	"33-Q":	1171,
	"33-H":	901	,
	"34-L":	2191,
	"34-M":	1725,
	"34-Q":	1231,
	"34-H":	961	,
	"35-L":	2306,
	"35-M":	1812,
	"35-Q":	1286,
	"35-H":	986	,
	"36-L":	2434,
	"36-M":	1914,
	"36-Q":	1354,
	"36-H":	1054,
	"37-L":	2566,
	"37-M":	1992,
	"37-Q":	1426,
	"37-H":	1096,
	"38-L":	2702,
	"38-M":	2102,
	"38-Q":	1502,
	"38-H":	1142,
	"39-L":	2812,
	"39-M":	2216,
	"39-Q":	1582,
	"39-H":	1222,
	"40-L":	2956,
	"40-M":	2334,
	"40-Q":	1666,
	"40-H":	1276
}

look_up = str(v) + '-' + str(ecl)
total_bits = total_cwd[look_up] * 8
difference = total_bits - len(out)

if(difference > 3):
	out += '0' * 4
else:
	out += '0' * difference

modulo = abs(len(out)%8 - 8) 	# add zeros to the right
out += '0' * modulo			 	# to make a multiple of 8

out += '1110110000010001' * int((total_bits - len(out))/16)
out += '11101100' * int((total_bits - len(out))/8)

# convert binary codewords to decimal coefficients for message polynomial's coefficients

coeffs = []
for i in range(0,128,8):
	coeffs.append((int(out[i:i+8],2)))


''' ERROR CORRECTION '''

log_table = [1,2,4,8,16,32,64,128,29,58,116,232,205,135,19,38,76,152,45,90,180,117,234,201,143,3,6,12,24,48,96,192,157,39,78,156,37,74,148,53,106,212,181,119,238,193,159,35,70,140,5,10,20,40,80,160,93,186,105,210,185,111,222,161,95,190,97,194,153,47,94,188,101,202,137,15,30,60,120,240,253,231,211,187,107,214,177,127,254,225,223,163,91,182,113,226,217,175,67,134,17,34,68,136,13,26,52,104,208,189,103,206,129,31,62,124,248,237,199,147,59,118,236,197,151,51,102,204,133,23,46,92,184,109,218,169,79,158,33,66,132,21,42,84,168,77,154,41,82,164,85,170,73,146,57,114,228,213,183,115,230,209,191,99,198,145,63,126,252,229,215,179,123,246,241,255,227,219,171,75,150,49,98,196,149,55,110,220,165,87,174,65,130,25,50,100,200,141,7,14,28,56,112,224,221,167,83,166,81,162,89,178,121,242,249,239,195,155,43,86,172,69,138,9,18,36,72,144,61,122,244,245,247,243,251,235,203,139,11,22,44,88,176,125,250,233,207,131,27,54,108,216,173,71,142,1]



# for now it will be hard-coded :)
# ec_blocks for 1-M => 10
ec_x = range(10,-1,-1) # 10..0
ec_l = [0,251,67,46,61,118,70,64,94,32,45] # this is the generator polynomial


# multiply generator by the lead exponent of message
# ec_x[0]-1 = 9
expnts = range(total_cwd[look_up]+ec_x[0]-1, ec_x[0]-1, -1)

# the lead term of the generator polynomial should also have the same exponent as the message polynomial
ec_x = [x + (expnts[0]-ec_x[0]) for x in ec_x]




''' STEP 1A '''

# multiply the generator polynomial by the lead term of the message polynomial (coeffs[0])

ec_alpha = [(x + (log_table.index(coeffs[0])))%255 for x in ec_l]

# convert alpha to decimal.:-

# RESULT FROM 1A
ec_decimal = [log_table[x] for x in ec_alpha]


''' STEP 1B '''

xor = []
for i in range(11):
	xor.append(coeffs[i] ^ ec_decimal[i])

# remaining xors that are zero
for i in range(11,16):
	xor.append(coeffs[i])

# RESULT FROM 1B
xor.pop(0)

'''
i don't understand this part right now
is the message polynomial updated to the
result of the xor, or is the xor indepd.?
'''
expnts = [x - 1 for x in expnts]

''' STEP 2A '''

ec_alpha = [(x + (log_table.index(xor[0])))%255 for x in ec_l]
ec_decimal = [log_table[x] for x in ec_alpha]

# same as above
ec_x = [x - 1 for x in ec_x]


''' STEP 2B '''

xor2 = []
for i in range(len(ec_decimal)):
	xor2.append(xor[i] ^ ec_decimal[i])

# remaining xors that are zero
for i in range(len(ec_decimal),len(xor)):
	xor2.append(xor[i])

xor2.pop(0)


''' DRAW IMAGE '''

# different colours as shortcuts
wt = (255,255,255)
bl = (0,0,0)
fi = (0,0,255)
vi = (0,255,255)

# initializing image framework
img = np.zeros((n,n,3), np.uint8)
img[:,:] = (128,128,128)

''' Format Information Area reservation '''
for i in range(8):
	img[i,8] = img[8,i] = img[8,8] = fi  # top-left
	img[8,n-i-1] = fi  # top-right
	img[n-i-1,8] = fi  # top-right
	
''' Version Information Area reservation '''
img[n-11:n-8,0:6] = vi
img[0:6,n-11:n-8] = vi

	
''' Timing Patterns '''

# always start and end with a dark module

for i in range(n):
	if(i%2 == 0):
		img[6,i] = img[i,6] = bl
	else:
		img[6,i] = img[i,6] = wt
		

''' Finder Patterns '''
# building the basic structure
fp = np.zeros((9,9,3), np.uint8)
fp[0:9,0:9] = wt # separator
fp[1:8,1:8] = bl
fp[2:7,2:7] = wt
fp[3:6,3:6] = bl

# placing finders onto the image
img[0:8,0:8] = fp[1:,1:] # top-left
img[0:8,n-8:n] = fp[1:,:8] # top-right
img[n-8:n,0:8] = fp[:8,1:] # bottom-left

''' Alignment Patterns '''

# qr-codes having version > 2 need to have
# certain fixed sizes as in the reference
# array below
apr = [[],[],[6,18],[6,22],[6,26],[6,30],[6,34],[6,22,38],[6,24,42],[6,26,46]] # and so on ...

# building the basic structure
ap = np.zeros((5,5,3), np.uint8)
ap[0:5,0:5] = bl
ap[1:4,1:4] = wt
ap[2,2] = bl

# computing viable options

# future optimization: only check three corner ap's

# now that I think of it, maybe not. because anyway
# you will have to compute indexes for placements

for i in range(len(apr[v])):
	for j in range(len(apr[v])):
	
		x = apr[v][i]
		y = apr[v][j]
	
		r = range(0,8)
		s = range(n-8,n)
		
		# check if in range, if not, place it
		print('placing finders on grid:')
		if(x in r and y in r or x in r and y in s or x in s and y in r):
			print(x,y,': not viable')
		else:
			print(x,y,': viable, inserting...')
			img[x-2:x+3,y-2:y+3] = ap

''' Dark Module '''
img[[(4 * v) + 9], 8] = bl

plt.imshow(img)
#plt.show()
