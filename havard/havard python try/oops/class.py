class point():
    def __init__(self , x , y ) :
        self.x  = x 
        self.y= y
    def double_x(self):
        self.x = self.x * 2

p = point(2,8)
print(p.x)
print(p.y)

p.double_x()

print(p.x)
print(p.y)