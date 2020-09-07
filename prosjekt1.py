from random import shuffle

def spill_runde():
		deck_round = list(range(1,14))*4
		shuffle(deck_round)
		board_array = [-1]*13 # 13 posisjoner (0-12 index)
		deck_empty = False
		i = 0
		antall_win = 0
		while len(deck_round) != 0:
			if all([board_array[k] == k+1 for k in range(13)]):
				antall_win += 1
				print("WIN!")
				break
			elif board_array[i%13] != i%13 + 1:
				board_array[i%13] = deck_round.pop(0)
			i += 1
		return antall_win

if __name__ == "__main__":
	n_runde, runde = 1000000, 1
	antall_win = 0
	while runde <= n_runde: #en loop er en runde med spillet
		antall_win += spill_runde()
		runde += 1
	print("Ferdig")
	print("Sansynelighet for å vinne({} runder): {}".format(n_runde,antall_win/n_runde))

