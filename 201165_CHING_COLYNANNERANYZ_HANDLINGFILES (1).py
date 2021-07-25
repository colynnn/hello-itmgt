#!/usr/bin/env python
# coding: utf-8

# In[4]:


# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.
products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}


# In[9]:


#CODE CELL 
#PROBLEM 1

def get_product(product): 
    return(products[product])
    
get_product("frappuccino")


# In[10]:


#CODE CELL 
#PROBLEM 2

def get_property(product, price): 
    return (products[product][price])
    
get_property("cappuccino","price")


# In[11]:


# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.  

# ADJUST THE NUMBER OF TABS AS NECESSARY TO FORMAT IT NICELY.
print('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
{code}\t\t\t{name}\t\t\t{quantity}\t\t\t{subtotal}

Total:\t\t\t\t\t\t\t\t\t\t{total}
==
''')


# In[12]:


# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.  

# Example:
print('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
cappuccino\t\tCappuccino\t\t1\t\t\t\t170.0
brewedcoffee\t\tBrewed Coffee\t\t5\t\t\t\t550.0

Total:\t\t\t\t\t\t\t\t\t\t720.0
==
''')


# In[1]:


#CODE CELL 
#PROBLEM 3

def main(): 
    
    #all products 
    menu = []
    americano = 0 
    brewedcoffee = 0 
    cappuccino = 0 
    espresso = 0 
    dalgona = 0 
    frappuccino = 0 
    
    #inputting orders 
    while True: 
        customer_order = input("Input order: ")
    
        if customer_order == "/": 
            break 

        #quantities of order 
        order_list = order.split (",")
        product = order_list [0]
        qty = int (order_list [1])

        if product == "americano": 
            americano += qty 

        elif product == "brewedcoffee":
            brewedcoffee += qty 

        elif product == "cappuccino":
            cappuccino += qty 

        elif product == "dalgona": 
            dalgona += qty 

        elif product == "espresso": 
            espresso += qty 

        elif product == "frappuccino": 
            frappuccino += qty 

        else: 
            menu.append(product)
        
        #adding items
        
        menu.sort()
        
        for n in range(len(menu)):
            
            if menu[n]=="americano":
                americano = get_product("americano")[qty]
                
            elif menu [n] == "brewedcoffe": 
                brewedcoffee = get_product ("brewedcoffee")[qty]
                
            elif menu [n] == "cappuccino": 
                cappuccino == get_product ("cappuccino")[qty]
                
            elif menu [n] =="dalgona": 
                dalgona == get_product ("dalgona") [qty]
            
            elif menu [n] == "espresso": 
                espresso == get_product ("espresso") [qty]
                
            elif menu [n] == "frappuccino": 
                frappuccino == get_product("frappuccino") [qty]
                
            else: 
                continue 
                
            
            
        #making the receipt 
        
        total = 0 
        
        with open ("receipt.txt", "w") as r: 
            r.write ("CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL")
            
            
        for i in range (len(menu)): 
            product = menu [i]
            name = get_property (product, "name")
            
            quantity = get_property (product, "qty")
            
            subtotal = quantity *get_property(product, "price")
            
            total += subtotal
            
            
        if product == "frappuccino": 
            r.write("CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL")
            r.write (f"{product}\t\t\t{name}\t\t\t{quantity}\t\t\t{subtotal}")
            r.write (f"Total:\t\t\t\t\t\t\t\t\t\t{total}")
            
        else: 
            r.write("CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL")
            r.write (f"{product}\t\t\t{name}\t\t\t{quantity}\t\t\t{subtotal}")
            r.write (f"Total:\t\t\t\t\t\t\t\t\t\t{total}")
            
        
main()
  

