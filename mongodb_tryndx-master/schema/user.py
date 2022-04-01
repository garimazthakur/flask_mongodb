schema = {"firstName":{"required":True, "type":"str",
                      "min":2,"max":20,"regex":'^[a-zA-Z]+$'},
          "lastName":{"required":True, "type":"str",
                      "min":2,"max":20,"regex":'^[a-zA-Z]+$'},
        #   "full_name":{"required":False, "type":"str",
        #               "min":0,"max":100,"regex":'^[a-zA-Z]+$'}
          "email":{"required":True, "type":"str",
                      "min":2,"max":100,"regex":'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'},
          "phone":{"required":True, "type":"int",
                      "min":7,"max":15,"regex":'^[0-9]*$'},
          "password":{"required":True, "type":"str",
                      "min":8,"max":20000,"regex":"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"},
                      }