print("MD. shahriar parvez! ")
print("02/27/2026")

from utils import add, subtract, multiply,divide

try:
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 0))
except Exception as e:
    print("Error:", e)