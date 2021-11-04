def extfib(sequence, to_add):
	for x in range(20):
		count = 0;
		for y in to_add:
			count += sequence[x + y]
		sequence.append(count)
	
	for i in sequence:
		print(i)
		
	print("-----------------------------")

# X X
extfib([0, 1], [0, 1])
# X _ X
extfib([0, 0, 1], [0, 2])
# X X _ _
extfib([0, 1, 0, 0], [0, 1])
# X X _
extfib([-1, 0, 1], [0, 1])