import ramdom

def countdown_dado(lados):
    while lados > 0:
       no = ramdom.randint(1,6)
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")