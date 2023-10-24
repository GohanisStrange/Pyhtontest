# не явная типизация  это:
# spa = 1
# kik = 'solid'
# nic = 1.2
#
# явная типизация это:
# m:int = 2
# s:str = 'string'

# не явную типизацию уже знает Python а явную указываем мы
def calc(a: int,m: int):
    return a*m
calc(5,25)
spam = (['friend','home','mama'])
spammer2 = (23)
def spammer(message:list)-> int:
    return len(message)
print(spammer(spam))

#генератор случайных чисел def check_queue(clients):
# for client in clients:
# yield client
# all_clients = ['Pasha', 'Jordan', 'Vika']
# hospital = check_queue(all_clients)
# print(hospital)
# next(generator)
# выводит переданныеы yield
# значения по очереди
# Aiohttp - асинхронная библиотека для взаимодействия с
# http/сайтами
# Позволяет максимально быстро собрать/
# взаимодействовать с веб сайтами
# Напрямую связан с asyncio


# Команды для
# подключения к сайту
# import aiohttp
# import asyncio
# async def main():
# async with aiohttp.ClientSession() as session:
# response = await session.get('какой сайт')
# web_content = await response.text()
# print(web_content)
# asyncio.run(main())