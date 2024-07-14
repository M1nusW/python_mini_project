def get_mask_card_number(mask: str) -> str:
    '''Принимает на вход номер карты и возвращает маску.'''
    if len(mask) != 16:
        return "Маска должна быть равна 16 символов"
    return mask[0:4] + " " + mask[4:6] + "** **** " + mask[12:]


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску."""
    str_account_number = str(account_number)
    mask_account_number = "**" + str_account_number[-4:]
    return mask_account_number
