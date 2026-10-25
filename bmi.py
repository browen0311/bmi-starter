# BMI 計算機：輸入體重和身高，算出 BMI
w = float(input("體重（公斤）："))
h = float(input("身高（米）："))
bmi = w / (h * h)
print("你的 BMI 是", round(bmi, 1))
