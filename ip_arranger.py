import re
import sys

def arrange(text):
    items = re.split(r'[\s,]+', text.strip())
    items = [i for i in items if i]
    return ', '.join(items)

def main():
    if len(sys.argv) > 1:
        # Accept input directly as arguments
        print(arrange(' '.join(sys.argv[1:])))
    else:
        print("Paste your IPs/subnets (one per line or space-separated).")
        print("Press Enter twice (blank line) when done:\n")
        lines = []
        while True:
            try:
                line = input()
                if line == '':
                    break
                lines.append(line)
            except EOFError:
                break
        result = arrange('\n'.join(lines))
        print("\nResult:")
        print(result)

if __name__ == '__main__':
    main()
