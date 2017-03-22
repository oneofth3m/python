class A:
  def __init__(self, i, j):
    self.i = i
    self.j = j

  def __repr__(self):
    return str(self.__dict__)

class B:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return str(self.__dict__)

if __name__ == "__main__":
  a=A(1,2)
  b=B(a,3)
  print b
