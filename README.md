# 🧠 Python Sorting Algorithms

A collection of **sorting algorithm implementations in Python**, maintained by the **Full Stack Engineers Club**.

This repository is designed to help developers **learn, practice, and master sorting algorithms**—a fundamental concept in computer science and software engineering.

---

## 🚀 About

Sorting algorithms are used to arrange data in a specific order (ascending or descending), which is essential for efficient searching, data processing, and optimization. :contentReference[oaicite:1]{index=1}  

This repo provides clean, easy-to-understand Python implementations of common sorting techniques, making it ideal for:

- 📚 Learning Data Structures & Algorithms (DSA)
- 💻 Coding interview preparation
- 🧠 Understanding time & space complexity
- 🤝 Open-source collaboration

---

## 📂 Algorithms Included

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Radix Sort *(if included)*

> Each algorithm is implemented in a separate file with clear logic and comments.

---

## ⚡ Example

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
