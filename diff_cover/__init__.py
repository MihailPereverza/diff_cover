from tool import parse_args, generate_report
import sys

if __name__ == "__main__":
    arg_dict = parse_args(sys.argv)
    generate_report(arg_dict)
