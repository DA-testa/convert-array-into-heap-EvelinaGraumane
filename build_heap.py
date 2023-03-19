# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(len(data) // 2,-1,-1):
        down(i,data,swaps)

    return swaps

    


def down(i,data,swaps):
    right = 2*i+2
    left = 2*i+1
    min = i

    if left < len(data) and data[left] < data[min]:
        min = left
    if right < len(data) and data[right] < data[min]:
        min = right

    if i != min:
        data[i], data[min] = data[min], data[i]
        swaps.append((i, min))
        down(min, data, swaps)

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    inputs = input()
    if "I" in inputs:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in inputs:
        inputs2 = input()
        if "a" not in inputs2:
            with open("./tests/"+inputs2, mode='r') as fails:
                n = int(fails.readline())
                data = list(map(int,fails.readline().split()))
    else:
        print("error")
        return

    # input from keyboard
    

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
