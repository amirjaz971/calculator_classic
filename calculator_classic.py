import math

class Calculator:
    def __init__(self,num,result,opt):
        self.num=num
        self.result=result
        self.opt=opt
        
    def show_result(self):
        print(f'Result={self.result}')
        
    def sqrt(self):
        self.result=math.sqrt(self.result)        
        
    def pow(self):
        self.result=math.pow(self.result,self.num)
     
    def clr(self):
        self.result=0 
    def add(self):
        self.result+=self.num
        
    def sub(self):
        self.result-=self.num
        
        
    def mul(self):
        self.result*=self.num    
                    
    def div(self):
        self.result/=self.num
        
    def floor(self):
        self.result=math.floor(self.result)    
        
    def abs(self):
        self.result=abs(self.result)
        
    def fact(self):
        self.result=math.factorial(int(self.result)) 
        
    def gcd(self):
        self.result=math.gcd(int(self.result),int(self.num))   
    def lcm(self):
        self.result=math.lcm(int(self.result),int(self.num))   
    def sin(self):
        self.result=math.sin(self.result)   
    def cos(self):
        self.result=math.cos(self.result)   
    def tan(self):
        self.result=math.tan(self.result)   
    def cot(self):
        self.result=(math.cos(self.result)/math.sin(self.result))
        
    def log(self):
        self.result=math.log10(self.result)   
        
    def per(self):
        self.result=self.result/100     
        
    def invert(self):
        self.result=1/self.result
           
    def correlate(self):
        self.result=(-1)*self.result
    def bin(self):
        self.result=bin(int(self.result))    
last_operations=[]

c1=Calculator(0,0,'')

print('Version 1.1')
on=True
while on:
            
            try:
                try:
                    c1.show_result()
                    
                    c1.num=float(input('Number:'))
                    last_operations.append(c1.num)
                    c1.result=c1.num
                    while True:
                        print('H.HELP')
                        c1.opt=input('Operator:')
                        last_operations.append(c1.opt)
                        
                        if c1.opt=='+':
                             c1.num=float(input('Number:'))
                             c1.add()
                             c1.show_result()
                             
                             last_operations.append(c1.result)
                        
                        elif c1.opt=='-':
                             c1.num=float(input('Number:'))
                             c1.sub()
                             c1.show_result()
                             last_operations.append(c1.result)
                        
                        elif c1.opt=='*':
                             c1.num=float(input('Number:'))
                             c1.mul()
                             c1.show_result()
                             last_operations.append(c1.result)
                        elif c1.opt=='/':
                             c1.num=float(input('Number:'))
                             print(f'The divide remaining of {c1.result}/{c1.num} is:{c1.result%c1.num}')
                             last_operations.append(c1.result%c1.num)
                             c1.div()
                             
                             c1.show_result()
                             last_operations.append(c1.result)
                             
                        elif c1.opt=='!':
                             c1.fact()
                             c1.show_result()
                             last_operations.append(c1.result)
                        
                        elif c1.opt=='[]':
                             c1.floor()
                             c1.show_result()
                             last_operations.append(c1.result)
                        
                        
                        elif c1.opt=='||':
                             c1.abs()
                             c1.show_result()
                             last_operations.append(c1.result)
                                
                        elif c1.opt.upper()=='ON':
                             print('The calculator is already ON!')
                         
                        elif c1.opt.upper()=='OFF':
                             on=False
                             
                             print('Exiting....')
                             break
                                    
                        elif c1.opt=='^':
                             c1.num=int(input('Number:'))
                             c1.pow()
                             c1.show_result()
                             last_operations.append(c1.result)
                            
                        elif c1.opt=='=' :
                             c1.show_result() 
                        
                        elif c1.opt.lower()=='clr':
                             c1.clr()
                             last_operations.append(c1.result)
                             break
                            
                            
                        elif c1.opt.lower()=='sq':
                             c1.sqrt()
                             c1.show_result()
                             last_operations.append(c1.result)
                             
                                
                        elif c1.opt.lower()=='lcm':
                             c1.num=int(input('Number:'))
                             c1.lcm()
                             c1.show_result()
                             last_operations.append(c1.result)
                        elif c1.opt.lower()=='gcd':
                             c1.num=int(input('Number:'))
                             c1.gcd()
                             c1.show_result()
                             last_operations.append(c1.result)
                        elif c1.opt.upper()=='LO':
                             print(f'Last operations={last_operations}')
                             
                             
                        elif c1.opt.lower()=='sin':
                             c1.sin()
                             c1.show_result()
                             last_operations.append(c1.result)
                             
                             
                             
                        elif c1.opt.lower()=='cos':
                             c1.cos()
                             c1.show_result()
                             last_operations.append(c1.result)
                             
                        elif c1.opt.lower()=='tan':
                             c1.tan()
                             c1.show_result()
                             last_operations.append(c1.result)
                             
                             
                        elif c1.opt.lower()=='cot':
                             c1.cot()
                             c1.show_result()
                             last_operations.append(c1.result)
                             
                             
                        elif c1.opt.lower()=='log':
                             c1.log()
                             c1.show_result()
                             last_operations.append(c1.result)

                                   
                        elif c1.opt=='%':
                             c1.per()
                             c1.show_result()
                             last_operations.append(c1.result)
                        elif c1.opt.lower()=='inv':
                             c1.invert()
                             c1.show_result()
                             last_operations.append(c1.result)
                             
                        elif c1.opt.lower()=='cor':
                             c1.correlate()
                             
                             c1.show_result()
                             last_operations.append(c1.result)  
                             
                        elif c1.opt.lower()=='bin':
                             c1.bin()
                             c1.show_result()
                             last_operations.append(c1.result)
                             c1.result=0
                                                            
                        elif c1.opt.upper()=='H':
                            
                             print('+:Addition')
                             print('-:Subtraction')
                             print('*:Multiplication')
                             print('/:Division')
                             print('%:Percent')
                             print('!:Factorial')
                             print('^:Power')
                             print('sq:Sqrt')
                             print('sin:sin')
                             print('cos:cos')
                             print('tan:Tan')
                             print('cot:Cot')
                             print('clr:clear')
                             print('off:Off')
                             print('[]:Bracket')
                             print('||:Floor')
                             print('log:Log10')
                             print('abs:Absolute')
                             print('gcd:Greatest common divisor')
                             print('lcm:Least common multiple')
                             print('lo:Last operations')
                             print('=:Equivalent')
                             print('inv:Invert')
                             print('cor:Correlate')
                             print('bin:Binary')
                             
                        else:
                            print('This operator is not defined!')
                            
                
                
                
                
                
                except ZeroDivisionError:
                    print('Can not divide by zero')    
            except ValueError:
                print('Invalid value!')    
    
    
    
    
    