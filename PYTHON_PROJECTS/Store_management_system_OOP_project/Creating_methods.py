class Item:
    def claculate_total_price(self,x, y):
        return x*y

        ''' 
        Pyhton passes the object itself as the first argument by default, whenever we define a new method.

        That is why we are not allowed to create methods that will never receive parameters(arguments).

        This argument is by default called as "self", hence calling itself, but there is not restriction to
        rename this argument, since it is not a reserved keyword.
            
        But it is accepted as a convention by most developers to leave the name of the first argument in the method 
        as "self", to make the code easier and readable for the user as well as the executer.  

        '''

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
item1.claculate_total_price(item1.price,item1.quantity)

item2 = Item()
item2.name = "Phone"
item2.price = 100
item2.quantity = 5
