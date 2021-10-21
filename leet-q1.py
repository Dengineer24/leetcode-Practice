class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        for i in range(n):
            if i % 3 == 0 and i % 5 == 0:
                output.append('FizzBuzz')
            elif i % 3 == 0:
                output.append('Fizz')
            elif i % 5 == 0:
                output.append('Buzz')
            else:
                value = i
                output.append(str(value))
        return output
            