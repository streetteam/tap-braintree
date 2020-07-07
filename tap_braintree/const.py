DEFAULT_TIMESTAMP = "1970-01-01T00:00:00Z"
LOOKBACK_WINDOW_DAYS = 2

# Decimal places according to ISO 4217, taken from https://en.wikipedia.org/wiki/ISO_4217
CURRENCY_DECIMAL_PLACES = {
    # zero
    'BIF': 0,
    'CLP': 0,
    'CVE': 0,
    'DJF': 0,
    'GNF': 0,
    'ISK': 0,
    'JPY': 0,
    'KMF': 0,
    'KRW': 0,
    'PYG': 0,
    'RWF': 0,
    'UGX': 0,
    'UYI': 0,
    'VND': 0,
    'VUV': 0,
    'XAF': 0,
    'XOF': 0,
    'XPF': 0,
    # one
    'MGA': 1,
    'MRU': 1,
    # three
    'BHD': 3,
    'IQD': 3,
    'JOD': 3,
    'KWD': 3,
    'LYD': 3,
    'OMR': 3,
    'TND': 3,
    # all other currencies have two decimal places
}