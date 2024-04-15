from 9_rectangle import Rectangle  # Assuming 9_rectangle.py contains the Rectangle class

class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        super().__init__(size, size)  # Initialize Rectangle with size as width and height
        self.__size = size

