result = []
def divider(a, b):
  if a < b:
    raise ValueError
  if b > 100:
    raise IndexError
  return a/b
try:
  data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
  for key, value in data.items():
    try:
      res = divider(int(key), value)
      result.append(res)
    except Exception as e:
      print(f"\nПомилка з ключем '{key}' та значенням '{value}':")
      print(f"Тип винятку: {type(e).__name__}")
      print(f"Повідомлення: {e}")
except Exception as e:
  print(e)
print(result)