/******************************************************************************
Zenith Kile
COMS 3213
9/5/23
*******************************************************************************/

#include <iostream>

using namespace std;

void insertionSort(int arr[], int n)
{
    int i, key, j;

    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }

        arr[j + 1] = key;
    }
}

void print(int arr[], int n)
{
    for (int a = 0; a < n; a++)
        cout << arr[a] << " ";
    cout << endl;
}

int main()
{
    int arr[] = { 12, 11, 13, 5, 6 };
    int num = sizeof(arr) / sizeof(int);

    insertionSort(arr, num);
    print(arr, num);

    return 0;
}





