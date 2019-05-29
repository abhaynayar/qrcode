from matplotlib import pyplot as plt


from tables import *
from draw import *


'''
Glossary

ccp_X	character capacities array (X => ecl)
mode	mode of data {N,A,B,K}
inp		input text by the user to be converted
ecl		error correction level {L,M,Q,H}
v		version
n		dimension
out		output data
img		final image
cci		character count indicator => determines in padded binary how many characters in input
'''


# https://www.thonky.com/qr-code-tutorial/


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

for x in range(1,len(inp),2):
	sum = alpha_dict[inp[x-1]] * 45 + alpha_dict[inp[x]]
	out += ("{0:b}".format(sum)).zfill(11)

if(len(inp)%2 == 1): # if it's odd
	out += ("{0:b}".format(alpha_dict[inp[-1]])).zfill(6)


''' Codewords & Padding '''

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

# convert binary codewords to decimal coefficients, for message polynomial's coefficients

coeffs = []
for i in range(0,128,8):
	coeffs.append((int(out[i:i+8],2)))


''' ERROR CORRECTION '''

# for now it will be hard-coded :)
# ec_blocks for 1-M => 10
ec_x = range(10,-1,-1) # 10..0


# multiply generator by the lead exponent of message
# ec_x[0]-1 = 9
expnts = range(total_cwd[look_up]+ec_x[0]-1, ec_x[0]-1, -1)


# the lead term of the generator polynomial should also have the same exponent as the message polynomial
ec_x = [x + (expnts[0]-ec_x[0]) for x in ec_x]


''' THE DIVISION PROCESS '''

for j in range(len(expnts)):
	ec_alpha = [(x + (log_table.index(coeffs[0])))%255 for x in ec_l]
	ec_decimal = [log_table[x] for x in ec_alpha]
	
	xor = []
	
	if len(coeffs) > len(ec_decimal):
		for i in range(len(ec_decimal)):
			xor.append(coeffs[i] ^ ec_decimal[i])

		for i in range(len(ec_decimal),len(coeffs)):
			xor.append(coeffs[i])
			
	else:
		for i in range(len(coeffs)):
			xor.append(coeffs[i] ^ ec_decimal[i])

		for i in range(len(coeffs),len(ec_decimal)):
			xor.append(ec_decimal[i])

	xor.pop(0)
	coeffs = xor


print(coeffs)
plt.imshow(img)
plt.show()
