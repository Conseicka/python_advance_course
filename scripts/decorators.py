from datetime import datetime as dtime
import time
def execution_time(func):
    def wrapper(*args,**kwargs):
        initial_time = dtime.now()
        func(*args, **kwargs)
        final_time = dtime.now()
        time_elapsed = final_time - initial_time
        print (f"Pasaron {time_elapsed.total_seconds()} segundos")
    return wrapper

@execution_time
def time_func():
    time.sleep(3)

@execution_time
def suma(a:int, b:int) -> int:
    return a + b

def saludo(nombre="Erick"):
    print("HOLA" + nombre)


time_func()
suma(5,5)
saludo("David")
