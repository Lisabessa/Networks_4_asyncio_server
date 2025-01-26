import asyncio

HOST = 'localhost'
PORT = 9095

async def tcp_echo_client(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    
    while True:
        message = input('Введите сообщение: ')
    
        # Отправка сообщения на сервер
        writer.write(message.encode())
        # Убеждаемся, что данные отправлены
        await writer.drain()  

        # Чтение ответа от сервера
        data = await reader.read(100)
    
        print(data.decode())

        if message.lower() == 'exit':
            break

    # Закрытие соединения
    writer.close()
    await writer.wait_closed()


# Запуск клиента
asyncio.run(tcp_echo_client(HOST, PORT))
