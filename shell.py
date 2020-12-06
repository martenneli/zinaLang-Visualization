from baisc import handel

while True:
  text = input('zena > ')
  result, error = handel.run(text)

  if error: print(error.as_string())
  else: print(result)