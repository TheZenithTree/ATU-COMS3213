/******************************************************************************
Zenith Kile
COMS 3213
9/7/23

Best Case of Insertion Sort: O(n) - List already sorted
Worst Case of Insertion Sort: O(n^2) - List sorted in opposite order than that which was requested
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
        while (j >= 0 && arr[j] < key)
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
    int arr[] = { 35, 99, 12, 45, 6, 7, 89, 1, 45, 3};
    int num = sizeof(arr) / sizeof(int);

    insertionSort(arr, num);
    print(arr, num);

    return 0;
}





