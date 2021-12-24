a = 12
s = "hello"

try:
  print(a+s)
except Exception as ex:
  print('{} Exception has occured.'.format(type(ex).__name__))
