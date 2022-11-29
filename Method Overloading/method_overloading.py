class Shop:

    def product(self,a, b, c=0):
       if c>0:
        print(a+b+c)
       else:
        print(a+b) 

a = Shop()
a.product(10, 22)
a.product(10,20,30)
