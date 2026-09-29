from enum import Enum
class Category(Enum):
    FOOD = "food"
    TRAVEL = "travel"
    BILLS = "bills"

print(Category.FOOD)
print(Category.FOOD.value)