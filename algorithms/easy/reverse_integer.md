Problem : https://leetcode.com/problems/reverse-integer/

Solution : Python3

```python
class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        reversed = 0
        negative = x < 0


        while num != 0:
            reversed = (reversed * 10) + (num % 10)
            num //= 10

        if reversed > 2**31 - 1:
            return 0

        if negative:
            return -reversed
        else:
            return reversed
```
