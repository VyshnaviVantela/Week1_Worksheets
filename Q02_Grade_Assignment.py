def Assign_grade(score):
  if score < 0 or score > 100:
    return "Invalid Score"
  elif score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
    
# 95, 85, 75, 65, 55, and 105
print(Assign_grade(95))
print(Assign_grade(85))
print(Assign_grade(75))
print(Assign_grade(65))
print(Assign_grade(55))
print(Assign_grade(105))


    
