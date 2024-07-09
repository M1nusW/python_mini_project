from src.masks import get_mask_card_number, get_mask_account

date = "2024-03-11T02:26:18.671407"


def mask_account_cart(type_and_number_cart: str) -> str:
    """Функция принимает тип и номер карты или номер счета выводя их замаскированными  """
    split_numbers_cart = type_and_number_cart.split()
    new_list = []
    name_and_number = []
    for numb_or_name in split_numbers_cart:
        if numb_or_name.isalpha():
            name_and_number.append(numb_or_name)
        elif numb_or_name.isdigit():
            if len(numb_or_name) == 16:
                masks_numb_cart = get_mask_card_number(numb_or_name)
                name_and_number.append(masks_numb_cart)
                new_list.append(name_and_number)
                name_and_number = list()
            elif len(numb_or_name) == 20:
                masks_numb_account = get_mask_account(numb_or_name)
                name_and_number.append(masks_numb_account)
                new_list.append(name_and_number)
                name_and_number = list()
        else:
            continue
    ready_data = ""
    for values_cart in new_list:
        translate_into_a_line = " ".join(values_cart)
        ready_data += (translate_into_a_line + "\n")
    return ready_data


def get_data(raw_date: str) -> str:
    """Функция, которая принимает данные о датеи прочего, и выводит только дату"""
    slice_date = raw_date[:10]
    date_clear = ""
    for one_symbol in range(len(slice_date)):
        if slice_date[one_symbol].isdigit():
            date_clear += slice_date[one_symbol]
        else:
            date_clear += " "
    date_clear_split = date_clear.split()
    split_date = date_clear_split[::-1]
    final_result = ".".join(split_date)
    return final_result


if __name__ == "__main__":
    print(mask_account_cart)
    print(get_data(date))