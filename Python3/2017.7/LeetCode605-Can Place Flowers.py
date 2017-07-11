'''
LeetCode605. Can Place Flowers
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
'''

class SolutionV2(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        length = len(flowerbed)
        if n == 0 :
            return True
        if length <= 2:
            return not 1 in flowerbed and n<2
        for i in range(length-1):
            if i==0 and flowerbed[0]==0:
                if flowerbed[1]==0:
                    flowerbed[0]=1
                    n-=1
            if i!=0:
                if flowerbed[i] == 0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    n-=1
        if flowerbed[-1]==0 and flowerbed[-2]==0:
            n-=1
        return n<=0

#【网友实现】:http://bookshadow.com/weblog/2017/06/04/leetcode-can-place-flowers/
class SolutionV3(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ans = 0
        for i, v in enumerate(flowerbed):
            if v: continue
            if i > 0 and flowerbed[i - 1]: continue
            if i < len(flowerbed) - 1 and flowerbed[i + 1]: continue
            ans += 1
            flowerbed[i] = 1
        return ans >= n