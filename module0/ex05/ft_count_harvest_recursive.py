def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    start = 1
    def recursion(start):
        if (start > days):
            print("Harvest time!")
            return
        print(f"Day {start}")
        recursion(start+1)
    recursion(start)