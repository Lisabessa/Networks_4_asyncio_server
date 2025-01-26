import asyncio

HOST = 'localhost'
PORT = 9095

async def handle_echo(reader, writer):
    client_address = writer.get_extra_info('peername')
    print(f'Подключен новый клиент: {client_address}')

    while True:
        # Чтение данных от клиента
        data = await reader.read(100)

        if not data:
            print("Отключение клиента")
            break

        message = data.decode()
        print(message)

        # Отправка данных обратно клиенту
        writer.write(data)
        # Убеждаемся, что данные отправлены
        await writer.drain()
    
    # Закрытие соединения
    writer.close()


async def main():
    server = await asyncio.start_server(handle_echo, HOST, PORT)

    # Вывод информации о сервере
    print(f'Сервер на {server.sockets[0].getsockname()}')

    async with server:
        await server.serve_forever()


# Запуск сервера
asyncio.run(main())
