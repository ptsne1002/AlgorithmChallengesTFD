
def find_result(testStr):
    mark = ""
    testStr += '.'
    finalStr = ""
    for index in range(len(testStr) - 1):
        currentVal = ord(testStr[index])
        nextVal  = ord(testStr[index + 1])
        if currentVal == nextVal:
            mark += testStr[index]
        else:
            mark += testStr[index]
            if currentVal > nextVal:
                finalStr += mark
            else:
                finalStr += mark + mark
            mark = ""
    return finalStr


if __name__ == "__main__":
    print("Input:")
    number_of_tests = input()
    data = [input() for i in range(int(number_of_tests))]
    print("Output:")
    index = 1
    for test in data:
        print(f"Case #{index}: {find_result(test)}")
        index += 1
