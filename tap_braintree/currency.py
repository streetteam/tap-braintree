from decimal import Decimal

from .const import CURRENCY_DECIMAL_PLACES


def get_amount_as_smallest_currency_unit(currency: str, amount: Decimal) -> int:
    """
    Given a decimal `amount` (eg. 19.34), convert it to the smallest unit in
    the given `currency` (eg, gbp: 1934). £19.34 -> 1934p.
    """
    decimal_places = CURRENCY_DECIMAL_PLACES.get(currency.upper(), 2)
    return int(amount * 10 ** decimal_places)
