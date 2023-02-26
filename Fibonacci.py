import pandas as pd

#numero a ser analisado
num = 1000
#sequencia de fibonacci
fibo = [0]


while fibo[-1] < num:
    
    if fibo[-1] == 0:
        
        fibo.extend([1])
        
    else:

        fibo.extend( [fibo[-1] + fibo[-2]])

    

print(f'sequencia:{fibo}')
if fibo[-1] == num:
    print('o Numero está na sequencia')
        




