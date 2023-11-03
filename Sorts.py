# cspell: disable
class Sorts:
    def Swap(arr: list, i: int, j: int):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def BubbleSort(arr: list):
        for i in range(len(arr) - 1):
            flag = True
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    Sorts.Swap(arr, j, j + 1)
                    flag = False
            if flag:
                break

    def Insertion(arr: list):
        # caso de i=0 inecesario
        for i in range(1, len(arr)):
            for j in range(i,0,-1):
                if arr[j] < arr[j-1]:
                    Sorts.Swap(arr,j,j-1)
                else:
                    break    

    def Selection(arr: list):
        for i in range(len(arr)-1):

            menor = i

            for j in range(i+1,len(arr)):

                if arr[j] < arr[menor]:
                    menor = j

            if menor != i:
                Sorts.Swap(arr, menor, i)
                     

               





"""
    optimizacion de Insertion: menos movimientos
    def Insertion(arr: list):
        for i in range(1, len(arr)):
            j = i
            pivot = arr[i]
            while j > 0 and pivot < arr[j - 1]:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = pivot
 """



if __name__ == "__main__":
    """
    test bubble sort
    arr = [9, 4, 6, 8, 5, 7, 1, 2, 3]
    print(arr)
    Sorts.BubbleSort(arr)
    print(arr)
    """

    '''
    test Selection sort
    arre = [9, 4, 6, 8, 5, 7, 1, 2, 3]
    print(arre)
    Sorts.Insertion(arre)
    print(arre)
    '''

    arre = [9, 4, 6, 8, 4, 7, 1, 2, 3]
    print(arre)
    Sorts.Selection(arre)
    print(arre)
