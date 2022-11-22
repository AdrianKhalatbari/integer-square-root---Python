Algorithm development: calculating “integer square root”.
Let us say that for an integer 𝑛, the integer square root of 𝑛 is the integer 𝑚 such that the difference
𝑎𝑏𝑠(𝑛 − 𝑚2)
is the smallest possible. The solution can be found by the following two steps:
1. Ask the user for a number.
2. Make a loop that searches for the integer that, when raised to the power of 2, is closest to the number given by the user.
For example, the integer square root of 7 is 3.
• 2 ** 2 = 4 – the distance is |7-4| = 3
• 3 ** 2 = 9 – the distance is |7-9| = 2.
Note that integer square root is always unique, that is, for an 𝑛, there cannot be two 𝑚:s which are equally far from 𝑛2.