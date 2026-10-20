x_test = [[i, j] for i in ["Sunny", "Rainy", "Cloudy"] for j in ["Hot", "Mild"]]
y_test = ["No", "Yes", "No", "No", "Yes", "Yes"]

def test(func):
  score = 0
  total = 0
  for i in range(len(x_test)):
    instance = x_test[i]
    answer = y_test[i]
    if func(instance[0], instance[1]) == answer:
      score += 1
    total += 1
  return ((score / total) * 10000 + 0.5) // 1 / 100
