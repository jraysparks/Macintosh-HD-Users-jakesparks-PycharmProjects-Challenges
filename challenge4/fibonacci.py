class Fibonacci:

    def fibo(self, n):
        x, y = 0, 1
        for i in range(n):
            x, y = y, x + y
        return x




# class Fibonacci:
#
#     def fibo(self, n):
#         if n < 0:
#             print("Incorrect input")
#             # First Fibonacci number is 0
#         elif n == 1:
#             return 0
#         # Second Fibonacci number is 1
#         elif n == 2:
#             return 1
#         else:
#             x = self.fibo(n-1)
#             y = self.fibo(n-2)
#             return x + y
#
#
#     # Driver Program
#

