# -*- coding: utf-8 -*-
"""
Created on Sun Jul 4313 11:39:18 2025

@author: aarav
"""
import pandas as pd


def Menu(choice):
    while choice not in ['1','2','3']:
        print('1: Numeric Intergration')
        print('2: Trigo Intergration')
        print('3: End Program')
        choice = input('Please enter your preferred option: ')
    return(int(choice))

def NumIntergration(count, coeff):
    ranges = range(0,100)
    ranges = [str(i) for i in ranges]
    
    while count not in ranges: 
        count = input('Please input the highest power in the equation: ')
        print('')
    
    count = int(count) 

    for power in reversed(range(0,count +1)):  
        while coeff not in ranges : 
            coeff = input(f'Please enter the coefficent for the term with {power} power: ')
            print('')
        power += 1
        coeff = int(coeff)/power
        powerlist.append(power -1)
        coefflist.append(coeff)
    
    table = pd.DataFrame({'Power': powerlist, 'Coeff':coefflist})
    print(table)
    
def TrigoIntergration(countT,func, coeff, funclist, coeffA):
    ranges = range(0,100)
    ranges = [str(i) for i in ranges]
    
    while countT not in ranges: 
        countT = input('Please input the no of trigo terms in the equation: ')
        print('')
    
    for idx in range(1,countT +1):
        while func not in ['0','1','2'] : 
            print('Sin = 0, Cos = 1, Sec^2 = 2')
            func = input(f'Please enter the function for the {idx} term: ')
            print('')
        
        if func == 0:
            funclist.append('-Cos')
        elif func == 1: 
            funclist.append('Sin')
        elif func == 2:
            funclist.append('Tan')
        
        while coeff not in ranges : 
            coeff = input(f'Please enter the coefficent for the {idx} term: ')
            print('')
                
        while coeffA not in ranges : 
            coeffA = input(f'Please enter the coefficent of the variable in the {idx} term: ')
            print('')        
        
        coefflist.append[coeff/coeffA]
        table = pd.DataFrame({'Function': funclist , 'Coeff':coefflist})
        print(table)
        
        
while True:
    count = 'a'
    coefflist = []
    powerlist = []
    coeff = 'a'
    coeffA = 'a'
    choice = 'a'
    countT = 'a'
    func = 0 
    funclist = []
    choice = Menu(choice)
    if choice == 1:
        NumIntergration(count, coeff)
        print('')
    elif choice == 2: 
        TrigoIntergration(countT, func, coeff, funclist, coeffA)
        print('')
    elif choice == 3: 
        break
        
            