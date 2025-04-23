import argparse
import statistics
import math
import configparser


parser = argparse.ArgumentParser(prog='calc')


operation_group = parser.add_mutually_exclusive_group()
operation_group.add_argument('-s', '--sum', dest='operation', action='store_const', const='sum', help='calculate sum')
operation_group.add_argument('-a', '--avg', dest='operation', action='store_const', const='average', help='calculate average')
operation_group.add_argument('-m', '--min', dest='operation', action='store_const', const='min', help='find min')
operation_group.add_argument('-x', '--max', dest='operation', action='store_const', const='max', help='find max')





format_group = parser.add_mutually_exclusive_group()
format_group.add_argument('-f', '--float', dest='format', action='store_const', const='float', help='output as float')
format_group.add_argument('-i', '--int', dest='format', action='store_const', const='int', help='output as int')


parser.add_argument('numbers', nargs='+', help='numbers to operate on')


args = parser.parse_args()
config = configparser.ConfigParser()

if not config.read('config.ini'):
    print("Error: <config.ini> file couldnt be read, check if it exists or has a diffrent name")

if args.operation is None:
    #args.operation = "sum"
    args.operation =  config['DEFAULT']['default_operation']


if args.format is None:
    #args.format = "int"
    args.format = config['DEFAULT']['default_type']



converted_numbers = []
for num_str in args.numbers:
    try:
        num_float = float(num_str)
        if args.format == "int":
            if num_float.is_integer():
                converted_numbers.append(int(num_float))
            else:
                print(f"Error: '{num_str}' cannot be converted to int (has decimal part)")
        else:
            converted_numbers.append(num_float)
    except ValueError:
        print(f"Error: '{num_str}' is not a valid number")

args.numbers = converted_numbers



print(f"Chosen operation: {args.operation}")
print(f"Chosen format: {args.format}")
print(f"Number list: {args.numbers}")

if args.operation == "sum":
    result = sum(args.numbers)

elif args.operation == "average":
    result = statistics.mean(args.numbers)
    if args.format == "int":
        result = math.floor(result)

elif args.operation == "min":
    result = min(args.numbers)

elif args.operation == "max":
    result = max(args.numbers)

else:
    print("Error, unexpected operation, write <python calc.py -h> for help")

print(f"Result: {result}")