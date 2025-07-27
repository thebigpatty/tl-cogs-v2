SHOP_ROLES = {
    "bronze": {
        "id": 832708253430317056,
        "cost": 500_000,
        "payday": 12_500,
        "requires": None,
        "color": "Bronze"
    },
    "silver": {
        "id": 832708338180948018,
        "cost": 1_000_000,
        "payday": 17_500,
        "requires": "bronze",
        "color": "Silver / White"
    },
    "gold": {
        "id": 832708431714320394,
        "cost": 1_500_000,
        "payday": 25_000,
        "requires": "silver",
        "color": "Gold"
    },
    "immortal": {
        "id": 832710600719204392,
        "cost": 2_500_000,
        "payday": 35_000,
        "requires": "gold",
        "color": "Black"
    },
    "arcane": {
        "id": 832708460239912971,
        "cost": 4_000_000,
        "payday": 50_000,
        "requires": "immortal",
        "color": "Neon"
    }
}
