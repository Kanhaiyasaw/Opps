class parent:
    def f(self):
        print("parent class f method")
    def f1(self):
        print("parent class f1 method")

class child(parent):
    def f2(self):
        print("child class f2 method")

class grandchild(child):
    def f5(self):
        print("this is grand child f5 method")

ob1=grandchild()
ob1.f5()
ob1.f2()
ob1.f1()
ob1.f()