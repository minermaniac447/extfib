# extfib
Messing around with extending the fibbonacci sequence

Simulates a custom fibbonacci sequence, with a specified input set of numbers and list of what numbers will be added to form the next number in the sequence

For example, `extfib([0, 1], [0, 1])` simulates the normal fibonacci sequence of 0 1 1 2 3 5 8... This can be represented as starting set [0, 1], and an addition property of X X Y (or, to form Y, the two digits before it will be used)

As another example, `extfib([0, 0, 1], [0, 2])` simulates a sequence with starting set [0, 1] and addition property of X _ X Y, so the number two before each new term will be skipped. This results in a slower, different output sequence: 0 0 1 1 1 2 3 4 6...
