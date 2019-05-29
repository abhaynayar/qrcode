import numpy as np


''' Initializing data '''

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