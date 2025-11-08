# Assignment 3: Algorithm Efficiency and Scalability

**Author:** Shashwat Baral
**Course:** Algorithms and Data Structures (MSCS-532-B01)

## Overview

This repository contains the implementation and analysis for an assignment on algorithm efficiency. The project is divided into two main parts:

1.  **Randomized Quicksort:** An implementation of Quicksort that uses a random pivot. This is compared empirically against a Deterministic Quicksort (using the first element as a pivot) to demonstrate its robustness against worst-case inputs.
2.  **Hashing with Chaining:** An implementation of a hash table that uses chaining for collision resolution and dynamic resizing to maintain a low load factor.

A detailed theoretical analysis and a discussion of the empirical results are available in the `Assignment_3_Report.md` file.

## Repository Contents

-   `report/Assignment_3_Report.md`: The formal write-up and analysis for the assignment.
-   `randomized_quicksort.py`: Python code for Randomized and Deterministic Quicksort, including the empirical comparison test.
-   `hash_table.py`: Python implementation of a Hash Table with Chaining, including a demonstration in the `main` block.
-   `README.md`: This file.

## How to Run the Code

### Prerequisites

-   Python 3.x

### Part 1: Quicksort Comparison

To run the empirical comparison between Randomized and Deterministic Quicksort:

```bash
python src/randomized_quicksort.py
