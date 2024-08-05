import plotly.graph_objects as go
import numpy as np

def func3(x:np.ndarray):
    return np.sin(x[0])*np.sin(x[1])

def func1(x:np.ndarray):
    return np.square(x[0]+1)+np.square(x[1]+2)

def partial_derivative(func,x:np.ndarray,index:int,h:float=.0001):
    dx=x.copy()
    dx[index]=dx[index]+h
    return (func(dx)-func(x))/h

def tangent_surface(func,x0:np.ndarray):
    def surface(x:np.ndarray):
        return partial_derivative(func=func,x=x0,index=0)*(x[0]-x0[0])+partial_derivative(func=func,x=x0,index=1)*(x[1]-x0[1]) + func(x0)
    return surface

fun=func3
x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
x,y=np.meshgrid(x,y)
z=fun(np.array([x,y]))
z1=tangent_surface(fun,np.array([np.pi/2,np.pi/2]))(np.array([x,y]))
surf1=go.Surface(x=x,y=y,z=z,opacity=0.7)
surf2=go.Surface(x=x,y=y,z=z1)
fig=go.Figure(data=[surf1,surf2])
fig.show()