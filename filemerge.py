def merge(output_file, input_files):
    input_files_mine = list(input_files)
    while input_files_mine
    for input_file in input_files_mine[:]:
        if input_file.readline():
            output_file.write(input_file.readline())
        else:
            input_files_mine.remove(input_file)
            

if __name__ == "__main__":

    import sys

    input_files = [open(x) for x in sys.argv[1:]]
    merge(sys.stdout, input_files)
