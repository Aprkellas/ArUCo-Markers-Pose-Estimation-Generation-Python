from detect_aruco_images import detect


if __name__ == "__main__":
    types = {1 : "1: DICT_4X4_100",
             2 : "DICT_4X4_250",
             3 : "DICT_5X5_100",
             4 : "DICT_5X5_250"}
    input = input("Please Enter an exact type number (e.g 1, 2 etc)")

    type = types[input]

    
    