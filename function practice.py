#function worksheet
#lidia

def username():
    name = input("enter name:")
    print("farewell", name)
    
username()

#task2

def price(Price, Quantity):
    total = Price * Quantity
    print("your total is", total)
inputPrice = float(input("enter price:"))
inputQuantity = int(input("enter quantity:"))
price(inputPrice, inputQuantity)
                
            
#task3
def calculate_area(num):
    area = 3.14 * num * num
    return area
result = calculate_area(5)
print("the area is", result)

#task4
def calrectangle(lenght, width):
    
    area = lenght * width
    perimeter = lenght * 2 + width * 2
    return area, perimeter
#width =(5)
lenght = int(input("enter lenght:"))
width = int(input("enter width:"))
#lenght =(2)
area, perimeter = calrectangle(lenght, width)
print("area is", area, "perimetera", perimeter)

#task5


#task5