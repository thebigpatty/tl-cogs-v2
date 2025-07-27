SHOP_ROLES = {
    "bronze": {
        "name": "Bronze",
        "role_id": 832708253430317056,
        "payday": 12500,
        "cost": 500_000,
        "requires": None,
        "command": "!buybronze"
    },
    "silver": {
        "name": "Silver",
        "role_id": 832708338180948018,
        "payday": 17500,
        "cost": 1_000_000,
        "requires": "bronze",
        "command": "!buysilver"
    },
    "gold": {
        "name": "Gold",
        "role_id": 832708431714320394,
        "payday": 25000,
        "cost": 1_500_000,
        "requires": "silver",
        "command": "!buygold"
    },
    "platinum": {
        "name": "Platinum",
        "role_id": 832710600719204392,
        "payday": 35000,
        "cost": 2_500_000,
        "requires": "gold",
        "command": "!buyplatinum"
    },
    "arcane": {
        "name": "Arcane",
        "role_id": 832708460239912971,
        "payday": 50000,
        "cost": 4_000_000,
        "requires": "platinum",
        "command": "!buyarcane"
    }
}
