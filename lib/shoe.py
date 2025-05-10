#!/usr/bin/env python3

# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"  # Default condition
    
    def __repr__(self):
        return f"Shoe(brand='{self.brand}', size={self.size})"
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, value):
        if not isinstance(value, str) or value.strip() == "":
            print("Brand must be a non-empty string.")
        else:
            self._brand = value
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        elif value <= 0:
            print("Size must be a positive integer.")
        else:
            self._size = value
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

