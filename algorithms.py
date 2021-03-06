# selection sort algorithm

def select_sort(k):
    if len(k) == 0:
        print("Error: There are no values in the list to sort!")
    else:
        i = 0
        while i < len(k) - 1:
            j = i + 1
            while j < len(k):
                if k[j] < k[i]:
                    minimum = k[j]
                    k[j] = k[i]
                    k[i] = minimum
                j += 1
            i += 1
        print(k)

# insertion sort algorithm

def insert_sort(k):
    if len(k) == 0:
        print("Error: There are no values in the list to sort!")
    else:
        i = 1
        while i < len(k):
            j = i - 1
            while j >= 0:
                if k[j + 1] < k[j]:
                    minimum = k[j + 1]
                    k[j + 1] = k[j]
                    k[j] = minimum
                j -= 1
            i += 1
        print(k)