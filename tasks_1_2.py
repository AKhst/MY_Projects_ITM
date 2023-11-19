import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, filename="example.log", filemode="w")

def divide(a: int, b: int):
    try:
        # Logging input values
        logger.info(f'На вход поданы значения переменных a:{a}, b:{b}')
        # Checking for division by zero
        if b == 0:
            raise ZeroDivisionError("Попытка деления на ноль")
        # Performing division
        result = a / b
        # Logging the result
        logger.info(f'Привет, ваш результат деления: {result}')
        return result
    except (ValueError, ZeroDivisionError, Exception) as e:
        # Logging errors
        logger.error(f"Ошибка в модуле функции: {e}", exc_info=True)
    finally:
        # Logging information about the finally block
        logger.info("Этот блок выполняется всегда")

if __name__ == '__main__':
    try:
        # Getting input values from the user
        a, b = int(input("Введите значение a: ")), int(input("Введите значение b: "))
        # Calling the divide function
        result = divide(a, b)
        # Displaying the result
        print(f'Результат деления: {result}')
    except Exception as er:
        # Logging errors from the main block
        logger.error(f"Ошибка из основного блока программы: {er}", exc_info=True)
    finally:
        # Logging information about the finally block in the main block
        logger.info("Этот блок выполняется всегда")
