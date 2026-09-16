if __name__ == "__main__":

    x=12
    int_to_float = float(x)
    print(f"Before: {x} ({type(x)}), After: {int_to_float} ({type(int_to_float)})")

    y=17.5
    float_to_int = int(y)
    print(f"Before: {y} ({type(y)}), After: {float_to_int} ({type(float_to_int)})")

    z=36 
    int_to_str = str(z)
    print(f"Before: {z} ({type(z)}), After: {int_to_str} ({type(int_to_str)})")

    a="986"
    str_to_int = int(a)
    print(f"Before: {a} ({type(a)}), After: {str_to_int} ({type(str_to_int)})")

    b=0
    int_to_bool = bool(b)
    print(f"Before: {b} ({type(b)}), After: {int_to_bool} ({type(int_to_bool)})")