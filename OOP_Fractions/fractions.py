class Fraction:
    
    def __init__(self, num, dem):
        self.num = num
        self.dem = dem
        
    def __del__(self):
        print("The values have discarded")
        
    def __str__(self):
        return f'{self.num}/{self.dem}'
    
    def __gt__(self, other):
        if self.num * other.dem > self.dem * other.num:
            return True
        else: 
            return False
        
    def __ge__(self, other):
        if self.num * other.dem >= self.dem * other.num:
            return True
        else: 
            return False

    def __lt__(self, other):
        if self.num * other.dem < self.dem * other.num:
            return True
        else: 
            return False
        
    def __le__(self, other):
        if self.num * other.dem <= self.dem * other.num:
            return True
        else: 
            return False
    
    def __eq__(self, other):
        if self.num == other.num and self.dem == other.dem:
            return True
        else:
            return False
        
    def __ne__(self, other):
        if self.num != other.num and self.dem != other.dem:
            return True
        else:
            return False
            
    # Arithmetic Operators
    def __add__(self, other):
        return f'{self.num + other.num}/{self.dem + other.dem}'
    
    def __sub__(self, other):
        return f'{self.num - other.num}/{self.dem - other.dem}'
    
    def __mul__(self, other):
        return f'{self.num * other.num}/{self.dem * other.dem}'
    
    def __truediv__(self, other):
        total_num= self.num_mult_dem(other)
        total_dem= self.dem_mult_num(other)
        
        if total_num % total_dem == 0:
            return f'{total_num/total_dem}/{total_dem/total_dem}'
        elif total_dem % total_num == 0:
            return f'{(total_num/total_num)}/{total_dem/total_num}'
        else:
            return f'{total_num}/{total_dem}'
        
    def __floordiv__(self, other):
        total_num= self.num_mult_dem(other)
        total_dem= self.dem_mult_num(other)
        
        return f'{total_num//total_dem}/{total_dem//total_dem}' 
    
    def num_mult_dem(self, other):
        return self.num * other.dem
    
    def dem_mult_num(self, other):
        return self.dem * other.num
    
    # Type Conversion
    def __abs__(self):
        return f'{abs(self.num)}/{abs(self.dem)}'
    
    def __int__(self):
        return int(self.num / self.dem)
    
    def __float__(self):
        return float(self.num / self.dem)
    
    def __round__(self, nDigits):
        return f'{(self.num / self.dem):.{nDigits}f}'
    
    def __trunc__(self):
        return f'{self.num:.0f}/{self.dem:.0f}'
    
    def __ceil__(self):
        if self.num < 0 and self.dem < 0:
            return f'{self.num:.0f}/{self.dem:.0f}'
        elif self.num < 0:
            return f'{self.num:.0f}/{(self.dem+1):.0f}'
        elif self.dem < 0:
            f'{(self.num+1):.0f}/{self.dem:.0f}'
        else:
            return f'{(self.num+1):.0f}/{(self.dem+1):.0f}'
        
    def __floor__(self):
        if self.num > 0 and self.dem > 0:
            return f'{self.num:.0f}/{self.dem:.0f}'
        elif self.num > 0:
            return f'{self.num:.0f}/{(self.dem-1):.0f}'
        elif self.dem > 0:
            return f'{(self.num-1):.0f}/{self.dem:.0f}'
        else:
            return f'{(self.num-1):.0f}/{(self.dem-1):.0f}'
    