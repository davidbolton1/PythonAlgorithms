# Given ["Y", "E", "S"]
# Return ["S", "E", "Y"]

from typing import List

class Solution:
  def reverseString(self, s: List[int]) -> None:
    s[:] = s[::-1]
    print(s[:])
  reverseString(int, [1, 2, 3])

# This overwrites the memory at the byte itself.