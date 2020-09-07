import prosjekt1

antall_win = 0

if __name__ == "__main__":
	deck = list(range(1,14))*4
	antall_win = prosjekt1.spill_runde(deck)
	print(antall_win)