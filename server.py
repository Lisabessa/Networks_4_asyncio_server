import asyncio

HOST = 'localhost'
PORT = 9095

async def handle_echo(reader, writer):
    host, port = writer.get_extra_info('peername')
    print(f'Подключен новый клиент: [{host}:{port}]')

    while True:
        # Чтение данных от клиента
        data = await reader.read(100)

        if not data:
            print(f'Отключение клиента [{host}:{port}]')
            break

        message = data.decode()
        print(f'[{host}:{port}]: {message}')

        # Отправка данных обратно клиенту
        writer.write(data)
        # Убеждаемся, что данные отправлены
        await writer.drain()
    
    # Закрытие соединения
    writer.close()


async def main():
    server = await asyncio.start_server(handle_echo, HOST, PORT)

    # Вывод информации о сервере
    host, port = server.sockets[0].getsockname()
    print(f'Сервер на [{host}:{port}]')

    async with server:
        await server.serve_forever()


# Запуск сервера
asyncio.run(main())
