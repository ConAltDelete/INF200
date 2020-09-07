#%% ## TASK A
SUITS = ('C','S','H','D')
VALUES = range(1,14)

def deck_loop():
	deck = []
	for suit in SUITS:
		for val in VALUES:
			deck.append((suit,val))
	return deck

def deck_comp():
	return [(suit,val) for suit in SUITS for val in VALUES]

#%% ## TASK B
def squares_by_comp(n):
	return [k**2 for k in range(n) if k % 3 == 1]

def squares_by_loop(n):
	r = []
	for k in range(n):
		if k % 3 == 1:
			r.append(k**2)
	return r

#%% TASK C
def letter_freq(txt):
	txt = txt.lower()
	freq = {}
	for letter in txt:
		if letter in freq:
			freq[letter] += 1
		else:
			freq[letter] = 1
	freq = dict(sorted(freq.items(),key=lambda item:item[0]))
	return freq

#%% TASK D
from random import randint 

def gjetting():
	c = int(input('your guess: '))
	return c

def tilfeldig_tall():
	return randint(1,6) + randint(1,6)

if __name__ == "__main__":
	poeng = 3 # poeng
	riktig_løsning = tilfeldig_tall() 
	while gjetting() != riktig_løsning and poeng > 0:
		print('Wrong, try again!')
		poeng -= 1
	if poeng > 0:
		print("you won {} points".format(poeng))
	else:
		print("you lost. Correct answer: {}.".format(riktig_løsning))

#%% END
if __name__ == '__main__':
	if deck_loop() != deck_comp():
		print('ERROR! DECK!')
	if squares_by_comp(20) != squares_by_loop(20):
		print('ERROR! SQUARES!')
	print(letter_freq('Hi, Jim!'))