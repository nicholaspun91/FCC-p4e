class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        picture = ''
        for i in range(self.height):
            picture += '*' * self.width + '\n'
        return picture
    
    def get_amount_inside(self, shape):
        height_fit = self.height // shape.height
        width_fit = self.width // shape.width
        return height_fit * width_fit
        
    def __str__(self):
        return 'Rectangle(width='+str(self.width)+', height=' + str(self.height) + ')'
   
class Square(Rectangle):
    def __init__(self, side, width=1, height=1):
        self.side = side
        super().__init__(width, height)
        self.width = side
        self.height = side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_height(self, side):
        self.side = side
        self.width = side
        self.height = side
        
    def __str__(self):
        return 'Square(side=' + str(self.side) + ')'