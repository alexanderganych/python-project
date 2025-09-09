"""Модуль для работы с заказами клиентов."""


class CustomerDataClass:
    """Класс для работы с заказами клиентов."""

    def __init__(self, customer_id, customer_name):
        """Конструктор для создания клиента с заказом.

        Атрибуты:
        customer_id - идентификатор клиента
        customer_name - ФИО клиента
        orders - список заказов
        """
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.orders = []

    def add_order(self, order_object):
        """Добавление заказа в список."""
        self.orders.append(order_object)

    def get_total_amount(self):
        """Подсчет суммы заказов.

        Атрибуты:
        total - сумма заказов
        return - сумма всех total
        """
        total = 0
        for o in self.orders:
            total += o.amount
        return total


class OrderDataClass:
    """Класс для работы с заказами."""

    def __init__(self, order_id, amount):
        """Конструктор для создания заказа.

        Атрибуты:
        order_id - идентификатор заказа
        amount - сумма заказа
        """
        self.order_id = order_id
        self.amount = amount


def calculate_discount(customer_obj):
    """Вычисление скидки для заказа.

    Атрибуты:
    total_amount - сумма для конкретного заказа
    return - получаем скидку
    """
    total_amount = customer_obj.get_total_amount()
    return total_amount * 0.1 if total_amount > 1000 else 0


def print_customer_report(customer_obj):
    """Печатаем данные по заказам клиентов.

    Атрибуты:
    len_orders - количество заказов у клиента
    total_amount - сумма всех заказов клиента
    """
    print('Customer Report for:', customer_obj.customer_name)

    len_orders = len(customer_obj.orders)
    print('Total Orders:', len_orders)

    total_amount = customer_obj.get_total_amount()
    print('Total Amount:', total_amount)

    print('Discount:', calculate_discount(customer_obj))

    # Проверка деления на ноль
    if len_orders > 0:
        print('Average Order:', total_amount / len_orders)
    else:
        print('No orders')


def main_program():
    """Стартуем программу."""
    # Создание клиента "SAP Customer" и двух заказов
    c1 = CustomerDataClass(1, 'SAP Customer')
    o1 = OrderDataClass(101, 500)
    o2 = OrderDataClass(102, 800)

    # Добавляем оба заказа клиенту и выводим результат
    c1.add_order(o1)
    c1.add_order(o2)
    print_customer_report(c1)

    # Создание клиента "Empty Customer" без заказов и выводим результат
    c2 = CustomerDataClass(2, 'Empty Customer')
    print_customer_report(c2)


main_program()