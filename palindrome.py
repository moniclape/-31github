<<<<<<< HEAD
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        while(temp > 0):
            dig = temp % 10
            rev = rev * 10 + dig
            temp = temp // 10
        if x == rev:
            print(True)
        else:
=======
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        while(temp > 0):
            dig = temp % 10
            rev = rev * 10 + dig
            temp = temp // 10
        if x == rev:
            print(True)
        else:
>>>>>>> 2bbc78f77730b82c90c6c63e88b4228f3e05b5f1
            print(False)