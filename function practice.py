#function worksheet
#lidia
#function worksheet
#lidia

# def username():
#     name = input("enter name:")
#     print("farewell", name)
#     
# username()
# 
# #task2
# 
# def price(Price, Quantity):
#     total = Price * Quantity
#     print("your total is", total)
# inputPrice = float(input("enter price:"))
# inputQuantity = int(input("enter quantity:"))
# price(inputPrice, inputQuantity)
#                 
#             
# #task3
# def calculate_area(num):
#     area = 3.14 * num * num
#     return area
# result = calculate_area(5)
# print("the area is", result)
# 
# #task4
# def calrectangle(lenght, width):
#     
#     area = lenght * width
#     perimeter = lenght * 2 + width * 2
#     return area, perimeter
# #width =(5)
# lenght = int(input("enter lenght:"))
# width = int(input("enter width:"))
# #lenght =(2)
# area, perimeter = calrectangle(lenght, width)
# print("area is", area, "perimeter", perimeter)
# 
# #task5
# 
# def valid_temp(temp):
#     if temp < -50 or temp > 50:
#         return False
#     else:
#         return True
# temp = 25
# if valid_temp(temp):
#     print("the temp is valid,", temp, "degrees")
# else:
#     print("the temp is not valid,", temp, "degrees")
#     
#
#task 1
#05/02/2025

# def name():
#     name = input("enter name:")
#     print("hello", name)
# name()
# 
# #task2
# def ave(grade1, grade2):
#     average = (grade1 + grade2) / 2
#     return average
# grade1 = 3
# grade2 = 5
# average = ave(grade1, grade2)
# print(average)
# 
# #task3
# def classave(grades):
#     classaverage = sum(grades) / 10
#     return classaverage
# grades = (12, 90, 56, 78, 58, 98, 67, 87, 98, 87)
# classaverage = classave(grades)
# print(classaverage)
# 
#task4
# def validgrade(grade):
#     if grade < 100 and grade > 0:
#         return True
#     else:
#         return False
# grade = 98   
# if validgrade(grade):
#     print("valid")
# else:
#     print("invalid")

# #task5
#     
# grades = [67, 67, 78, 98, 87, 78, 78, 98, 90]
# def gradescal():
#     grade = int(input("enter grade:"))
#     if grade < 100 and grade > 0:
#         grades.append(grade)
#     else:
#         print("invalid")
#         
# 
# gradescal()
# print(grades)

# #task8
# def lowgrade(grade):
#     return min(grade)
# grade = [32, 45, 12, 98]
# 
# print(lowgrade(grade))

#task9#
# grades = [37, 78, 98, 87, 78, 78, 98, 90]
# def gradescal():
#     grade = int(input("enter grade:"))
#     if grade < 100 and grade >= 50:
#         grades.append(grade)
#     else:
#         print("invalid")
#    # if grades < 50 and grades >= 0:
#     #    grades.remove(grades)
#         
# 
# gradescal()
# print(grades)

#task10
# def count_pass(grades):
#     return sum(1 for grade in grades if grade >= 50)
# 
# def graderep(highest, lowest, ave):
#     highest = max(grades)
#     lowest = min(grades)
#     ave = sum(grades) / len(grades)
#     passing = count_pass(grades)
#     
#     print(highest)
#     print(lowest)
#     print(ave)
#     print(passing)
#grade_list = [85, 92, 47, 76, 50, 89, 33, 100, 67, 45, 76]
# graderep(highest, lowest, ave)
#

#task11
def medgrade(grade_list):
    grade_list.sort()
    print(grade_list)
grade_list = [85, 92, 47, 76, 50, 89, 33, 100, 67, 45, 76]
medgrade(grade_list)