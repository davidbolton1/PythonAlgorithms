
from typing import List

class Solution:
  def reverseString(self, s: List[str]) -> None:
    s[:] = s[::-1]
    print(s[:])
  reverseString(str, ["h", "e"])

