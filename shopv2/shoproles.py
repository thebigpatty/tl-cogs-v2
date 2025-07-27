SHOP_ROLES = {
    {
        "name": "Bronze",
        "role_id": 832708253430317056,
        "payday": 12500,
        "cost": 500_000,
        "command": "!buybronze"
    },
    {
        "name": "Silver",
        "role_id": 832708338180948018,
        "payday": 17500,
        "cost": 1_000_000,
        "requires": 832708253430317056,
        "command": "!buysilver"
    },
    {
        "name": "Gold",
        "role_id": 832708431714320394,
        "payday": 25000,
        "cost": 1_500_000,
        "requires": 832708338180948018,
        "command": "!buygold"
    },
    {
        "name": "Platinum",
        "role_id": 832710600719204392,
        "payday": 35000,
        "cost": 2_500_000,
        "requires": 832708431714320394,
        "command": "!buyplatinum"
    },
    {
        "name": "Arcane",
        "role_id": 832708460239912971,
        "payday": 50000,
        "cost": 4_000_000,
        "requires": 832710600719204392,
        "command": "!buyarcane"
    }
}
