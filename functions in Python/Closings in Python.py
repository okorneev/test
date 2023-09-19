#замыканием называется ситуация, когда вложенная функция пользуется переменными, которые не объявлены в ее теле
def main_func(name):
    def inner_func():
        print(f"Hello world, {name} says!")
    return inner_func()
b = main_func('Oleg')
print(b)