import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
              n1 = len(a)
              m1 = len(a[0])
              n2 = len(b)
              m2 = len(b[0])
              if m1 != m2:
                return -1
              c = np.matmul(a,b)
              return c